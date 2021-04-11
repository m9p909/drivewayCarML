from flask import Flask
from flask import request
from flask import abort
import base64
import sqlite3
import json
import pictureTaker
from database import setupDatabase


app = Flask(__name__)


def validateclean_score(number):
        return number <= 5 and number >= 1





def dataPost(image, clean_score=-1):
    '''Posts a valid input to database, receives image binary and optionally a value for 'clean_score'  
    
    This method is currently INVALID, it will not work properly'''
    return None
    con = setupDatabase()
    cur = con.cursor()
    cur.execute("insert into images(image) values (?)",
                ([sqlite3.Binary(image)]))
    if clean_score != -1:
        clean_score = int(clean_score)
        if validateclean_score(clean_score):
            cur.execute(
                "update images set clean_score=? where id=(select max(id) from images)", (clean_score,))

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
        if 'clean_score' in stuff:
            if validateclean_score(stuff['clean_score']):
                cur.execute('update images set clean_score=? where id=?',
                            (stuff['clean_score'], stuff['id']))
            else:
                abort(400)
    con.commit()
    return "success"


def dataDelete(id):
    con = setupDatabase()
    cur = con.cursor()
    cur.execute('delete from images where id=?', id)
    con.commit()


@app.route('/data', methods=['POST', 'GET', 'PUT', 'DELETE'])
def data():
    if request.method == 'POST':
        if 'file' in request.files:
            imagedata = request.files['file']
            if 'clean_score' in request.args:
                clean_score = request.args.get('clean_score')
                return dataPost(imagedata.read(), clean_score)
            else:
                return dataPost(imagedata.read())
        else:
            abort(400)
    if request.method == 'PUT':
        return dataPut(request.json)
    elif request.method == 'GET':
        return dataGet(request)
    elif request.method == 'DELETE':
        return dataDelete(request)


@app.route('/')
def hello_world():
   return 'Hello World'


if __name__ == '__main__':
    pictureTaker.runScheduledTasks()
    app.run(host="0.0.0.0")
