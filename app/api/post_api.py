from app.response import response


class PostApi(object):

    @staticmethod
    def on_post(req, resp):
        data = req.get_param('data')

		if data:
			response.ok(resp, data)
		else:
			response.err(resp, response.BAD_REQUEST, {'message': 'No postdata found'})
