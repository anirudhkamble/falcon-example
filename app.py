#!/usr/bin/env python

import falcon
from falcon_multipart.middleware import MultipartMiddleware

from api.get_api import GetApi
from api.post_api import PostApi


# initialize the falcon application
app = application = falcon.API(middleware=[MultipartMiddleware()])

app.add_route('/example/get/first', GetApi)
app.add_route('/example/post/first', PostApi)
