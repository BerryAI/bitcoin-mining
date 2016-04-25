
import json
import logging



# token for accessing the API hosted at this google app engine application.
ACCESS_TOKEN = "MpsI0PUj3ScKnn5cwUAiecUZ3wZ36kRi4ItxU3fD"



def check_token(func):
    def handler(self, *args, **kwargs):

        token = self.request.get("token", "")

        if token == "":
            logging.debug("Error: token missing")
            self.response.headers["Content-Type"] = "application/json"
            self.response.write(json.dumps({"status": "error", "message": "TOKEN_MISSING"}))
            return

        if token != ACCESS_TOKEN:
            logging.debug("Error: token invalid")
            self.response.headers["Content-Type"] = "application/json"
            self.response.write(json.dumps({"status": "error", "message": "TOKEN_INVALID"}))
            return

        # token is valid. continue the function

        return func(self, *args, **kwargs)

    return handler
#


def log_required_params(*ar):
    """
    Use of Decorator
    http://www.artima.com/weblogs/viewpost.jsp?thread=240845
    """
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            self = args[0]
            error_count = 0

            for param in ar:
                if not self.request.get(param):
                    logging.warning("Parameter \"" + param + "\" does not exist in the request")
                    error_count = error_count + 1

                else:
                    logging.debug(param + ' = \"' + self.request.get(param) + '\"')

            if error_count > 0:
                logging.error('Missing required parameters. Error message returned')
                self.response.headers["Content-Type"] = "application/json"
                self.response.write(json.dumps({"status": "error", "message": "PARAMETER_MISSING"}))
                return

            f(*args, **kwargs)

        return wrapped_f
    return wrap
#

