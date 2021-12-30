from flask import Flask, jsonify, request
from flask_cors import CORS
import sys

from pymongo import MongoClient
import boto3


s3 = boto3.resource('s3',aws_access_key_id='AKIA6OHLO6A3AEAIY75O',
aws_secret_access_key='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',
region_name='us-west-2')

app = Flask(__name__)
CORS(app)


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

@app.route('/user')
def user():
    name = request.args.get('name')
    url = request.args.get('url')
    video = {
        'name': name,
        'url': url
    }
    db.videos.insert_one(user)

    return 'Saved!', 201

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)