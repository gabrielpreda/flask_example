import logging

import os
import pickle
import pandas as pd
import numpy as np
from flask import abort

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier



logger = logging.getLogger('species')


class IrisModel:
    species_model = None
    path = None
    species_name = ['setosa', 'versicolor', 'virginica']

    def __init__(self, path=''):
        self.path = path
        self.species_model = None


        try:
            logger.info(path)
        except Exception as ex:
            logger.error(f"Error: {type(ex)} {ex}")
            abort(500)

    def load_resource(self, file_name):
        logger.info(file_name)
        return pickle.load(open(file_name, "rb"))

    def save_resource(self, resource, file_name):
        logger.info(file_name)
        pickle.dump(resource, open(file_name, "wb"))
    
    
    def train(self):
        status = -1
        try:
            iris = datasets.load_iris()
            
            # prepare the model data
            data_df = pd.DataFrame({
                'sepal_length':iris.data[:,0],
                'petal_length':iris.data[:,2],
            })
            
            X = data_df[['sepal_length', 'petal_length']]
            y = iris.target
            # prepare the model and fit it
            clf=RandomForestClassifier(n_estimators=100)
            clf.fit(X,y)
            
            # test the model
            
            sepal_length = 7.5
            petal_length = 7.1
            test_df = pd.DataFrame({'sepal_length':sepal_length, 'petal_length': petal_length},index=[0])
            predicted = clf.predict(test_df.values)[0]
            logger.info("Predicted value: {}".format(predicted))
            
            # save the model
            self.save_resource(clf, os.path.join(self.path, 'species.model'))
            
            status = 'Train OK'
            return status
        except Exception as ex:
            logger.error(f"Error: {type(ex)} {ex}")
            abort(500)


    def predict(self, sepal_length, petal_length):
 
        try:
            logger.info(sepal_length)
            logger.info(petal_length)
            
            if not self.species_model:
                self.species_model = self.load_resource(os.path.join(self.path, 'species.model'))
            test_df = pd.DataFrame({'sepal_length':sepal_length, 'petal_length': petal_length},index=[0])
            predicted = self.species_model.predict(test_df.values)[0]
            
            predicted_species = self.species_name[predicted]
            logger.info("Predicted value: {}".format(predicted))
            print(predicted_species)
            
            return predicted_species
        
        except Exception as ex:
            logger.error(f"Error: {type(ex)} {ex}")
            abort(500)


