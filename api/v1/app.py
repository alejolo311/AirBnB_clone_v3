#!/usr/bin/python3
"""
instance of Flask app
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
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
