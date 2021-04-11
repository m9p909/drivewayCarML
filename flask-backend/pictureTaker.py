from apscheduler.schedulers.background import BackgroundScheduler
from time import sleep
import atexit
from datetime import datetime
import os
import shutil
import traceback
from database import setupDatabase

onPi = False
if(os.uname()[4][:3] == 'arm'):
    from picamera import PiCamera
    onPi = True


def takePicture(id):
    """ Takes a picture with the webcam and returns the directory in ./tmp """
    if(onPi):
        path = '/home/pi/pictures/'+str(id)+'.jpg'
        camera = PiCamera()
        camera.start_preview()
        sleep(5)
        camera.capture(path)
        camera.stop_preview()
        return path
    # for debugging
    else:
        path = './pictures/'+str(id)+'.jpg'
        shutil.copyfile('./image.jpg', path)
        return path


def getNextId():
    con = setupDatabase()
    cur = con.cursor()
    cur.execute("select MAX(id) as id from images")
    res = cur.fetchone()
    if res[0] == None:
        return 1
    else:
        return res[0]
    con.close()


def insertIntoDB(path):
    con = setupDatabase()
    cur = con.cursor()
    cur.execute('insert into images(image) values (?)', [path])
    con.commit()
    con.close()


def createPicture():
    try:
        path = takePicture(getNextId())
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
