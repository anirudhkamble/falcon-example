import json

import falcon

from app.response import response


class GetApi(object):

    @staticmethod
    def on_get(req, resp):
        message = {'message': 'First Falon App..'}
        
        if isinstance(message, dict):
        	response.ok(resp, message)
        else:
        	response.err(resp, response.INTERNAL_ERROR, {'message': 'something went wrong!'})
