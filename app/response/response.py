import json

import falcon


SUCCESS = falcon.HTTP_200
BAD_REQUEST = falcon.HTTP_BAD_REQUEST
INTERNAL_ERROR = falcon.HTTP_500
NOT_FOUND = falcon.HTTP_404

content_type = 'application/json'


def ok(resp, message):
    resp.status = SUCCESS
    resp.content_type = content_type
    resp.data = json.dumps(message)


def err(resp, errCode, message):
    resp.status = errCode
    resp.content_type = content_type
    resp.data = json.dumps(message)
