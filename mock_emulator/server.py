import logging

from flask import Flask
from flask import request

app = Flask(__name__)

logging.basicConfig(filename='flask.log', level=logging.DEBUG)
logger = logging.getLogger('flask_server')

import inner_data_builder
import redwood


@app.before_request
def log_request_info():
    logger.info(request.get_data())


@app.route('/')
def home():
    main_message = "It works!!!"
    return main_message, 200


if __name__ == '__main__':
    app.run(port="5000", debug=True, host="0.0.0.0")
