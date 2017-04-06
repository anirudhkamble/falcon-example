#!/usr/bin/env python

import falcon
from falcon_multipart.middleware import MultipartMiddleware

from api.firstGet import FalconAppGet
from api.firstPost import FalconAppPost


# initialize the falcon application
app = application = falcon.API(middleware=[MultipartMiddleware()])

app.add_route('/example/get/first', FalconAppGet)
app.add_route('/example/post/first', FalconAppPost)

