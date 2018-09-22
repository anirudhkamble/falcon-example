
import falcon
from falcon_multipart.middleware import MultipartMiddleware

from app.middlewares import validator as _validator
from routes import routes as _routes


# initialize the falcon application

middlewares = [MultipartMiddleware(), _validator.DataValidator()]

app = application = falcon.API(middleware=middlewares)


# Initialize all api routes.
for apiRoute, apiClass in _routes.iteritems():
	app.add_route(apiRoute, apiClass)
