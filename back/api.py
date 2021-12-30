import os
import sys

import boto3
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from pymongo import MongoClient

load_dotenv()
s3 = boto3.resource('s3',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name='us-west-2'
)

app = Flask(__name__)
CORS(app)

app = Flask(__name__)

client = MongoClient('mongodb://mongodb:27017/')
db = client.VideoProcessingDB


@app.route('/')
def hello_world():
    s3.Object('video-processing-s3','videos/requirements.txt').upload_file('static/requirements.txt')
    return "BACKEND woring fine!"


@app.route("/upload", methods=["POST","GET"])
def search():
    data = request.data
    print('This is error output', file=sys.stderr)
    print(data, file=sys.stderr)
    return "HOLA"


@app.route('/video')
def users():
    collection = db.videos.find()

    item = {}
    data = []
    for element in collection:
        item = {
            'id': str(element['_id']),
            'name': element['name'],
            'url': element['url']
        }
        data.append(item)

    return jsonify(
        data=data
    )


@app.route('/save-video', methods=['POST'])
def save_video():
    name = request.args.get('name')
    # Guardar video en S3
    # return url
    url = 'AAAAAAAAAA'
    # Llamar a api de etiquetado, retorna lista de tags con minuto
    tags = [{'perro': '3:10'}, {'gato': '10:23'}, {'gato': '15:23'}, {'arbol': '10:23'}]
    video = {
        'name': name,
        'url': url,
        'duration': 20,
        'tags': tags,
    }
    db.videos.insert_one(video)

    return jsonify({
        'name': name,
        'url': url
    })


@app.route('/user')
def user():
    name = request.args.get('name')
    url = request.args.get('url')
    video = {
        'name': name,
        'url': url
    }
    db.videos.insert_one(video)

    return 'Saved!', 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
