from flask import Flask
from flask_mongoengine import MongoEngine

from models.video import Video

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': 'cloud_unsa'
}
db = MongoEngine(app)

@app.route('/test', methods=['GET'])
def test():
    Video(
        name='asd',
        duration=20.4,
        url='qweqwe'
    ).save()
    return {
        'success': True
    }

if __name__ == "__main__":
    app.run(debug=True)
