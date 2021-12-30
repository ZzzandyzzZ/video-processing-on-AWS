from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://mongodb:27017/')
db = client.VideoProcessingDB


@app.route('/')
def hello_world():
    return "BACKEND woring fine!"

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
