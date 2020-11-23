import os

from flask import (Flask, request, session)
from flask import Flask, flash, request, redirect, url_for
from flask.helpers import make_response
from werkzeug.utils import secure_filename
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    CORS(app)

    from . import movies, get_movies
    app.register_blueprint(movies.server)
    app.register_blueprint(get_movies.server)

    # a simple page that says hello
    # @app.route('/static/<string:pid>')
    # def getImage(pid):
    #     image_binary = read_image(pid)
    #     response = make_response(image_binary)
    #     response.headers.set('Content-Type', 'image/jpeg')
    #     response.headers.set('Content-Disposition',
    #                          'attachment',
    #                          filename='%s.jpg' % pid)
    #     return response

    return app