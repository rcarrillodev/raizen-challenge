import pandas
from pandas.core.frame import DataFrame
from sensors.model.data_model import Data

class CsvParser:

    dataFrame = None

    def __init__(self,csvPath) -> None:
        self.dataFrame = pandas.read_csv(csvPath)
        pass

    def query(self, field):
        result = []
        result.append(Data("10-01-1989",30.4,10.3,10))
        return result