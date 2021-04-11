import sqlite3
import os
onPi = False

if(os.uname()[4][:3] == 'arm'):
    onPi = True

def setupDatabase():
    return sqlite3.connect('carml.db')


def getPicturePath(id):
    if(onPi):
        path = '/home/pi/pictures/'+str(id)+'.jpg'
    else:
        path = './pictures/'+str(id)+'.jpg'
    return path