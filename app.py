from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    'db': 'cloud_unsa'
}
db = MongoEngine(app)

@app.route('/', methods=['GET'])
def test():
    return {
        'success': True
    }

if __name__ == "__main__":
    app.run(debug=True)
