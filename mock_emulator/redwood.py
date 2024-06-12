from __main__ import app

from flask import render_template


@app.route('/HttpServices/api/redwood_data/', methods=['GET', 'POST'])
def return_some_data():
    return render_template("redwood_data.json")
