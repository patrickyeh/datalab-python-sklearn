__author__ = 'Vetom'
from datalabsdk.Model import ClassificationModel
import numpy as np
from sklearn import linear_model

from datalabsdk.DataTransform import DataTransform

class SGDClassifierModel(ClassificationModel):
    def __init__(self):
        self.model = None

    def train(self,input_path,**param):
        obj_dt = DataTransform(input_path,param)
        obj_dt.scan_data_type()
        x,y = obj_dt.fetch_data()
        clf = linear_model.SGDClassifier()
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
        return self.model.predict(obj_array)

    def validate_by_object(self,obj_test_x,obj_test_y):
        return self.model.score(obj_test_x,obj_test_y)




if __name__ == '__main__':
    obj_model = SGDClassifierModel()
    obj_model.train('C:/data/a3a',n_features=123)
    print obj_model.validate_by_file('C:/data/a3a.t',n_features=123)
