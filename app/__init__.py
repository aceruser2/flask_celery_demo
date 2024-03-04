from flask import Flask
from flask_restx import Resource, Api

flask_app = Flask(__name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
flask_api = Api(flask_app, authorizations=authorizations)
