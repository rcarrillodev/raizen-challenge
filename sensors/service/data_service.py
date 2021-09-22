from sqlalchemy.sql.roles import OrderByRole
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
                if ':' in sortBy:
                    sortStatement = sortBy.split(':')
                    field = sortStatement[0]
                    order = sortStatement[1]
                    if order == 'ASC':
                        query = query.order_by(asc(getattr(Data, field)))
                    elif order == 'DESC':
                        query = query.order_by(desc(getattr(Data,field)))
                else:
                    query = query.order_by(text(sortBy))
            if range:
                field,lower,upper = range.split(':')
                query = query.filter(getattr(Data, field).between(lower,upper))
            if not limit:
                query = query.limit(10)
            else:
                query = query.limit(limit)
            models = query
        return models

