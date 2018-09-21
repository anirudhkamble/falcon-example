
import falcon
from falcon_multipart.middleware import MultipartMiddleware

from app.middleware import middleware as _middlewares
from app.api import get_api as _get
from app.api import post_api as _post


# initialize the falcon application

middlewares = [MultipartMiddleware(), _middlewares.DataValidator()]

app = application = falcon.API(middleware=middlewares)


app.add_route('/example/get/first', _get.GetApi)
app.add_route('/example/post/first', _post.PostApi)
