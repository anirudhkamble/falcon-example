from app.response import response


class GetApi(object):

    @staticmethod
    def on_get(req, resp):
        data = req.get_param('data')

        if data:
        	response.ok(resp, data)
        else:
        	response.err(resp, response.INTERNAL_ERROR, {'message': 'No Request data'})
