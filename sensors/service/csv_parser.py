import pandas
from pandas.core.frame import DataFrame

class CsvParser:

    dataFrame = None

    def __init__(self,csvPath) -> None:
        self.dataFrame = pandas.read_csv(csvPath)
        pass

    def getDataFrame(self) -> DataFrame:
        return self.dataFrame

    def getMaxCO2(self):
        pass