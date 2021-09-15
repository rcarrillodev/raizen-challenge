import json
import falcon
from pandas.core.frame import DataFrame

class Resource:
    dataSet = DataFrame()
    def __init__(self,dataSet) -> None:
        self.dataSet = dataSet
        pass
    def on_get(self,req,resp):
        test = self.dataSet.nlargest(1,'CO2')
        resp.text = test.to_json()
        resp.status = falcon.HTTP_200