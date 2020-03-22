import json
import logging
import logging.config
import os
import threading

from flask import Flask, jsonify, request, abort

from model.model import IrisModel

app = Flask(__name__)

logger = logging.getLogger('species')

@app.route('/status', methods=['GET'])
def status():
    logger.info("Request received")
    return jsonify({'status': "OK"})


@app.route('/train', methods=['GET'])
def train():
    try:
        logger.info('train')
        species_model = IrisModel()
        species_run = species_model.train()
        logger.info("Response sent")
        return jsonify({"train": species_run})
    except Exception as ex:
        logger.error(f"Error: {type(ex)} {ex}")
        abort(500)
        

@app.route('/species', methods=['POST'])
def species():
    try:
        sepal_length = request.json['sepal_length']
        logger.info(sepal_length)
        petal_length = request.json['petal_length']
        logger.info(petal_length)
        species_model = IrisModel()
        print(sepal_length, petal_length)
        species_prediction = species_model.predict(float(sepal_length), float(petal_length))
        logger.info("Response sent")
        return jsonify({"species": species_prediction})
    except Exception as ex:
        logger.error(f"Error: {type(ex)} {ex}")
        abort(500)

        
if __name__ == '__main__':
    app.run()
