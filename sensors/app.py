import falcon
import aumbry
from sensors.resources.data_resource import Resource as DataResource
from sensors.dao.db_manager import DBManager
from sensors.service.data_service import DataService
from sensors.config import AppConfig

basePath = '/sensors/v1'
cfg = aumbry.load(
        aumbry.FILE,
        AppConfig,
        {
            'CONFIG_FILE_PATH': './sensors/config.yml'
        }
    )
mgr = DBManager(cfg.db.connection)
data = DataResource(DataService(mgr))

app = application = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='*', allow_credentials='*'))

app.add_route(basePath + '/data',data) 