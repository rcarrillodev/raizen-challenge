import falcon
import json


class Resource:

    def __init__(self,dataService) -> None:
        self._dataService = dataService
        pass

    def on_get(self,req,resp):
        field = req.get_param('field')
        sort = req.get_param('sort')
        range = req.get_param('range')
        result = self._dataService.queryData(field)
        resp.text = json.dumps([d.to_dict() for d in result])
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200