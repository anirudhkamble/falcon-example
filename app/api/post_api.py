from app.response import response


class PostApi(object):

    @staticmethod
    def on_post(request, response):
        postData = ast.literal_eval(request.stream.read())

        if postData:
        	response.ok(resp, postData)
        else:
        	response.err(resp, response.BAD_REQUEST, {'message': 'No data found'})
