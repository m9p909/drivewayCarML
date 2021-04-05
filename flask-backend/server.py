from flask import Flask
from flask import request
from flask import abort
import base64
import sqlite3
import json


print("Opened database successfully")

app = Flask(__name__)

def validateNumCars(number):
        return number < 5 and number > 0
        


def setupDatabase():
    return sqlite3.connect('carml.db')

def dataPost(image, numcars=-1):
    '''Posts a valid input to database, receives image binary and optionally a value for 'numcars'  '''
    con = setupDatabase()
    cur = con.cursor()
    cur.execute("insert into images(image) values (?)", ([sqlite3.Binary(image)]))
    if numcars != -1:
        numcars = int(numcars)
        if validateNumCars(numcars):
            cur.execute("update images set numcars=? where id=(select max(id) from images)", (numcars,))
            
        
    con.commit()
    return 'success'
    
def dataGet(stuff):
    ''' gets a list of all the images in the db '''
    con = setupDatabase()
    cur = con.cursor()
    cur.execute('select * from images')
    return json.dumps(cur.fetchall())

def dataPut(stuff):
    con = setupDatabase()
    cur = con.cursor()
    if 'id' in stuff:
        if 'numcars' in stuff:
            if validateNumCars(stuff['numcars']):
                cur.execute('update images set numcars=? where id=?',(stuff['numcars'],stuff['id']))
            else:
                abort(400)
    con.commit()
    return "success"
        


def dataDelete(id):
    con = setupDatabase()
    cur = con.cursor()
    cur.execute('delete from images where id=?',id)
    con.commit()


@app.route('/data', methods=['POST','GET','PUT','DELETE'])
def data():
    if request.method == 'POST':
        if 'file' in request.files:
            imagedata = request.files['file']
            if 'numcars' in request.args:
                numcars = request.args.get('numcars')
                return dataPost(imagedata.read(), numcars)
            else:
                return dataPost(imagedata.read())
        else:
            abort(400)
    elif request.method == 'GET':
        return dataGet(request)
    elif request.method == 'DELETE':
        return dataDelete(request)


@app.route('/')
def hello_world():
   return 'Hello World'
        

if __name__ == '__main__':
   app.run()