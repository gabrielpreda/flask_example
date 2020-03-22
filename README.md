# Introduction

This is an example of using Flask to create an API for an Python program. 

The service is exposing several endpoints as following:

* GET /status - return the status of the service
* GET /samples - 1 parameter: spec - if provided, return this species cardinality, otherwise return all samples cardinality
* POST /prediction_class - 2 parameters: sepal_length & petal_length, predict the class (model is RandomForest)

# Source files

The following files are included in the project:
* train_model.py - script to train the model; a RandomForest model is trained to predict the species of iris
* app.py - API using Flask; to predict the species, a pretrained model (build in train_model.py) is load

# Usage

To start the service, run `python app.py`