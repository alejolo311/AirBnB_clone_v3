#!/usr/bin/python3
"""
instance of Flask app
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS
from flasgger import Swagger


app = Flask(__name__)
template = {
  "swagger": "2.0",
  "info": {
    "title": "HBNB API RESTful",
    "description": "this API is a Holberton School project build by Alejo \
    López & Hugo Bayona, this API is part of the AirBnB clone project",
    "version": "1.0.0"
  },
  "schemes": [
    "http",
  ],
  "operationId": "getmyData"
}
swagger_config = {
    "headers": [
    ],
    "specs": [
        {
            "endpoint": 'hbnb',
            "route": '/hbnb.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, template=template,  config=swagger_config)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False
cors = CORS(app, resources={"*": {"origins": "0.0.0.0"}})

port = getenv("HBNB_API_PORT") or 5000
ip = getenv("HBNB_API_HOST") or '0.0.0.0'


@app.teardown_appcontext
def teardown(self):
    """teardown close the storage"""
    storage.close()


@app.errorhandler(404)
def resource_not_found(error):
    """404 return"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host=ip, port=port, threaded=True)
