import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

SAModel = declarative_base()


class Data(SAModel):
    __tablename__ = 'data'

    data_id = sa.Column(sa.Integer, primary_key= True)
    time = sa.Column(sa.Integer)
    temp = sa.Column(sa.Integer)
    co2 = sa.Column(sa.Integer)
    humidity = sa.Column(sa.Integer)

    def __init__(self, time=None, temp=None, co2=None, humidity=None):
        self.time = time
        self.temp = temp
        self.co2 = co2
        self.humidity = humidity

    @property
    def as_dict(self):
        return {
            'time': self.username,
            'temp': self.company,
            'co2': self.score,
            'humidity': self.humidity
        }

    


