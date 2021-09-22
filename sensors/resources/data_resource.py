import falcon
import json


class Resource:

    def __init__(self,dataService) -> None:
        self._dataService = dataService
        pass

    def on_get(self,req,resp):
        sortBy = req.get_param('sort-by')
        range = req.get_param('range')
        limit = req.get_param('limit')
        result = self._dataService.queryData(sortBy,range,limit)
        resp.text = json.dumps([d.to_dict() for d in result])
        resp.content_type = falcon.MEDIA_JSON
        resp.status = falcon.HTTP_200