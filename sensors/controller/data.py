import json
import falcon
from pandas.core.frame import DataFrame

class Resource:
    dataSet = DataFrame()
    def __init__(self,dataSet) -> None:
        self.dataSet = dataSet
        pass
    def on_get(self,req,resp):
        field = req.get_param('field')
        print(field)
        return 'holi'