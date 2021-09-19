from sensors.service.csv_parser import CsvParser
import falcon
from .controller.data import Resource
from .service.csv_parser import CsvParser

app = application = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='*', allow_credentials='*'))
csvParser = CsvParser('sensors/resources/sensor-data.csv')
sensorsDataFrame = csvParser.getDataFrame()
data = Resource(sensorsDataFrame)
app.add_route('/sensors/v1/data',data) 