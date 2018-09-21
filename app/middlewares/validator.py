import ast


class DataValidator(object):

    def process_request(self, req, resp):

        data = {}

        try:
            for key in req.params:
                data.update({key: req.get_param(key)})

            req._params = {}
            postData = str(req.stream.read())

            if len(postData) != 0 and req.accept:
                data.update(dict(ast.literal_eval(postData)))
        except SyntaxError as s_ex:
            print 'SyntaxError Exception:', s_ex.message
        except Exception as ex:
            print 'Exception occurred:', ex.message

        if data:
            req._params['data'] = data
