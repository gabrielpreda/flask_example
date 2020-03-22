# Introduction

This is an example of using Flask to create an API for an Python program. 

The service is exposing several endpoints as following:

* GET /status - return the status of the service
* GET train - train the model IrisModel, from model module
* POST /species - 2 parameters: sepal_length & petal_length, predict the class by calling the predict function of model module (model is RandomForest)

# Source files

The following files are included in the project:
* model/model.py - module containinin the IrisModel class: train the model, predict using the trianing model 
* app.py - API using Flask; to predict the species, a pretrained model (build in model.py using) is load

# Usage

To start the service, run `python app.py`