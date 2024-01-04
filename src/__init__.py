from flask import Flask, jsonify
from flask_restx import Resource, Api


# instantiate the app
app = Flask(__name__)

api = Api(app)

app.config.from_object('src.config.DevelopmentConfig')


@app.route('/about')
def hello_world():
    return 'Hello World!'


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'test message'
        }


api.add_resource(Ping, '/ping')
