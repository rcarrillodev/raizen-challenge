import falcon
from pandas.core.frame import DataFrame
from sensors.service.csv_parser import CsvParser
from sensors.controller.data_controller import Resource
from sensors.service.data_service import DataService

app = application = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='*', allow_credentials='*'))
basePath = '/sensors/v1'
csvParser = CsvParser('sensors/resources/sensor-data.csv')
data = Resource(DataService(csvParser))
app.add_route(basePath + '/data',data) 