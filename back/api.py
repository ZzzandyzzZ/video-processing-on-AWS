import json
import os
import sys
import requests as req

import boto3
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

load_dotenv()
s3 = boto3.resource('s3',
    aws_access_key_id=os.getenv('aws_access_key_id'),
    aws_secret_access_key=os.getenv('aws_secret_access_key'),
    region_name='us-west-2'
)

client = MongoClient('mongodb://mongodb:27017/')
db = client.VideoProcessingDB


@app.route('/')
def hello_world():
    return "BACKEND woring fine!"


@app.route("/upload", methods=["POST","GET"])
def search():
    s3_bucket_name = 'video-processing-s3'
    print('This is error output', file=sys.stderr)
    f = request.files['file']
    f.save(f.filename)
    s3.Object(s3_bucket_name,'videos/'+f.filename).upload_file(f.filename)
    #s3.Object(s3_bucket_name,'videos/'+ f.filename).download_file(f.filename)
    return {"response":"TODO OK"}


@app.route('/save-video', methods=['POST'])
def save_video():
    s3_bucket_name = 'video-processing-s3'
    f = request.files['file']
    f.save(f.filename)
    s3.Object(s3_bucket_name,'videos/'+f.filename).upload_file(f.filename)
    name = f.filename
    url = name
    ############################################
    #
    # Llamar a api de etiquetado, retorna lista de tags con minuto
    #
    ##########################################
    tags = [
        {
            '1': ['perro', 'gato', 'gato']
        },
        {
            '3': ['casa', 'loro', 'gato']
        },
    ]
    estructure_data = {}
    for item in tags:
        for values in list(item.values())[0].keys():
            if values not in estructure_data:
                estructure_data[values] = [list(item.keys())[0]]
            else:
                estructure_data[values].append(list(item.keys())[0])
    new_estructure = []
    for item,value in estructure_data.items():
        new_estructure.append({"tag":item,"min":value})

    video = {
        'name': name,
        'url': url,
        'duration': 20,
        'tags': new_estructure,
    }
    db.videos.insert_one(video)
    data = {
        "method": "post",
        "data": {
            "name": name,
            "tags": new_estructure
        }
    }
    response = req.post('https://i62ihnt2s4.execute-api.us-west-2.amazonaws.com/default/index_videos', json=data)
    if response.status_code != 200:
        return jsonify({
            'success': False
        })

    return jsonify({
        'success': True,
        'name': name,
        'url': url,
    })


@app.route('/search-video', methods=['GET'])
def search_video():
    # tag = request.args.get('tag')
    tag = "perro"
    data = {
        "method": "get",
        "data": {
            "tag": tag
        }
    }
    response = req.get('https://i62ihnt2s4.execute-api.us-west-2.amazonaws.com/default/index_videos', json=data)
    if response.status_code != 200:
        return jsonify({
            'success': False
        })
    response_data = json.loads(response.content.decode())
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
