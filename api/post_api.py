import ast
import json

import falcon


class PostApi(object):

    @staticmethod
    def on_post(request, response):
        # Convert post request data(json format) to dictionary
        post_data = ast.literal_eval(request.stream.read())
        # printing the post request data received
        response.status = falcon.HTTP_200
        response.content_type = 'application/json'
        # Sending it back as response by loading into request.data object
        response.data = json.dumps(post_data)
        return response
