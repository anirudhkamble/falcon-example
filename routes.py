from app.api import get_api as _get
from app.api import post_api as _post


# Dict mapping apis to their classes
routes = {
	'/example/get/first': _get.GetApi,
	'/example/post/first': _post.PostApi
}
