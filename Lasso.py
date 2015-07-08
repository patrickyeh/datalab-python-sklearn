__author__ = 'Vetom'
from datalabsdk.Model import ClassificationModel
import numpy as np
from sklearn import linear_model

from datalabsdk.DataTransform import DataTransform

class LassoModel(ClassificationModel):
    def __init__(self):
        self.model = None

    def train(self,input_path,**param):
        self.update_param(param)
        obj_dt = DataTransform(input_path,param)
        obj_dt.scan_data_type()
        x,y = obj_dt.fetch_data()
        clf = linear_model.Lasso(alpha=0.01)
        model = clf.fit(x,y)
        self.model = model

        return model

    def predict_by_file(self,input_path,**param):
        x,y = self._fetch_file(input_path,**param)
        return self.predict_by_object(x)

    def validate_by_file(self,input_path,**param):
        x,y = self._fetch_file(input_path,**param)
        return self.validate_by_object(x,y)

    def predict_by_object(self,obj_array):
        prdict_y = self.model.predict(obj_array)
        prdict_y[prdict_y>0] = 1
        prdict_y[prdict_y<=0] = -1
        return prdict_y

    def validate_by_object(self,obj_test_x,obj_test_y):
        return self.model.score(obj_test_x,obj_test_y)


