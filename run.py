
import falcon
from falcon_multipart.middleware import MultipartMiddleware

from app.middleware import middleware as _middlewares
from routes import routes as _routes


# initialize the falcon application

middlewares = [MultipartMiddleware(), _middlewares.DataValidator()]

app = application = falcon.API(middleware=middlewares)


# Initialize all api routes.
for apiRoute, apiClass in _routes.iteritems():
	app.add_route(apiRoute, apiClass)
