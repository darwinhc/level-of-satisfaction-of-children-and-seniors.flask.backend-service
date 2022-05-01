"""Application definition and service routes"""
from json import loads
from os import getenv

from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
# Local
from src.collect_data import collect_data
from src.load_model import load_model


app = Flask(__name__)
CORS(app)
MODEL_CHILD = load_model('models/' + getenv('MODEL_CHILD'))
FIELDS_CHILD = loads(getenv('FIELDS_CHILD'))


MODEL_SENIOR = load_model('models/' + getenv('MODEL_SENIOR'))
FIELDS_SENIOR = loads(getenv('FIELDS_SENIOR'))

MESSAGE_NO_FIELD = getenv("MESSAGE_NO_FIELD", "Fields are required to predict")


@app.route("/child", methods=["POST"])
def predict_child():
    data = collect_data(request.json, FIELDS_CHILD)
    if data is None:
        abort(400)
    return {"prediction": int(MODEL_CHILD.predict(data)[0])}


@app.route("/senior", methods=["POST"])
def predict_older_adult():
    data = collect_data(request.json, FIELDS_SENIOR)
    if data is None:
        abort(400)
    return {"prediction": int(MODEL_SENIOR.predict(data)[0])}
