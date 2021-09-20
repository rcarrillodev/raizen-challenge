from sensors.dto.data_dto import Data as DataDTO
from sensors.dao.model.data_model import Data
from sensors.service import DataAccessService
from sqlalchemy.sql import text
from sqlalchemy import desc,asc
class DataService(DataAccessService):

    def queryData(self, sortBy, range, limit):
        rawData = self.doQuery(self.db.session,sortBy,range,limit)
        result = [DataDTO(d.time, d.temp, d.co2, d.humidity) for d in rawData]
        return result
    

    def doQuery(self, session, sortBy, range, limit):
        with session.begin():
            query = session.query(Data)
            if sortBy:
                sortStatement = sortBy.split(':')
                if(sortStatement[1] == 'ASC'):
                    query = query.order_by(asc(text(sortStatement[0])))
                if(sortStatement[1] == 'DSC'):
                    query = query.order_by(desc(text(sortStatement[0])))
            if not limit:
                query = query.limit(10)
            else:
                query = query.limit(limit)
            models = query
        return models

