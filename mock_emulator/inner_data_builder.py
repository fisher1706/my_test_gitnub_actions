from __main__ import app

from flask import request

from generator import Generator
from mock_utils import Utils


@app.route('/HttpServices/api/inner/<data_type>', methods=['POST'])
def generate_inner_data(data_type):
    Utils().cleaner()
    resp = {"message": f"inner data for type {data_type} created"}
    error = {"error": f"inner data for type {data_type} was not created"}

    if data_type == "redwood":
        val = request.get_json().get("value")
        data = Generator().generate_some_data(data=val)
        Utils().writer(data=data, filename="redwood_data.json")
        response = resp
        status_code = 200
    else:
        response = error
        status_code = 404

    return response, status_code
