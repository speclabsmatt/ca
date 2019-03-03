from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .models import db, Author


@app.route("/", methods=['GET'])
def hello():
    authors = Author.query.all()
    return jsonify([Author.as_dict(author) for author in authors])
