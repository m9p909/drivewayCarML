from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
import atexit
from datetime import datetime
import os
import shutil
import traceback
import shared

onPi = shared.onPi
if(onPi):
    from picamera import PiCamera


def takePicture(id):
    """ Takes a picture with the webcam and returns the directory in ./tmp """
    path = shared.getPicturePath(id)
    
    if(onPi):
        camera = PiCamera()
        try:
            camera.start_preview()
            sleep(5)
            camera.capture(path)
        except:
            path = "ERROR NO PATH"
        finally:
            camera.stop_preview()
            return path

    # for debugging
    else:
        path = './pictures/'+str(id)+'.jpg'
        shutil.copyfile('./image.jpg', path)
        return path


def getNextId():
    con = shared.setupDatabase()
    cur = con.cursor()
    cur.execute("select MAX(id) as id from images")
    res = cur.fetchone()
    if res[0] == None:
        return 1
    else:
        return res[0]+1
    con.close()


def insertIntoDB(path):
    con = shared.setupDatabase()
    cur = con.cursor()
    cur.execute('insert into images(image) values (?)', [path])
    con.commit()
    con.close()


def createPicture():
    try:
        path = takePicture(getNextId())
        if path == "ERROR NO PATH":
            print("picture taking failed")
        else:
            insertIntoDB(path)
            print('Stored picture to '+path)
    except Exception as e:
        traceback.print_exc()


def runScheduledTasks():
    createPicture()
    scheduler = BackgroundScheduler()
    # jobs go here
    if(onPi):
        scheduler.add_job(func=createPicture, trigger="interval", hours=1)
    else:
        scheduler.add_job(func=createPicture, trigger="interval", seconds=30)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    createPicture()
