import json

import falcon


class GetApi(object):

    @staticmethod
    def on_get(request, response):
        message = {'message': 'First Falon App..'}
        response.status = falcon.HTTP_200
        response.content_type = 'application/json'
        response.data = json.dumps(message)
        return response
