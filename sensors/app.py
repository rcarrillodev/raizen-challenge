from sensors.service.csv_parser import CsvParser
import falcon
from .data import Resource
from .service.csv_parser import CsvParser

app = application = falcon.App()
csvParser = CsvParser('sensors/resources/sensor-data.csv')
sensorsDataFrame = csvParser.getDataFrame()
data = Resource(sensorsDataFrame)
app.add_route('/data',data) 