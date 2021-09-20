from sensors.dto.data_dto import Data
class DataService:

    def __init__(self, csvParser):
        self._csvParser = csvParser
        pass

    def queryData(self, field):
        rawData = self._csvParser.query(field)
        print(rawData)
        result = []
        for d in rawData:
            result.append(Data(d.time, d.temp, d.co2, d.humidity))
        return result
