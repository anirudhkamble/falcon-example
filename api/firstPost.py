import falcon
import json
import ast


class FalconAppPost(object):

    @staticmethod
    def on_post(request, response):
        # Convert post request data(json format) to dictionary
        postData = ast.literal_eval(request.stream.read())
        # printing the post request data received
        print postData
        response.status = falcon.HTTP_200
        response.content_type = 'application/json'
        # Sending it back as response by loading into request.data object
        response.data = json.dumps(postData)
        return response
