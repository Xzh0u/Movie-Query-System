from flask import (Blueprint, request, session)
# from flask import jsonify
from flask_cors import CORS
from flask import Response
from .search import MovieItems

server = Blueprint('movies', __name__, url_prefix='/get_movies')
CORS(server)


@server.route('/sorted_movies', methods=('GET', 'POST'))
def getSortedMovies():
    return 'Hello, World!'


@server.route('/taged_movies', methods=('GET', 'POST'))
def getTagedMovies():
    return 'Hello, World!'


@server.route('/typed_movies', methods=('GET', 'POST'))
def getTypedMovies():
    return 'Hello, World!'


@server.route('/all_movies', methods=('GET', 'POST'))
def getAllMovies():
    return 'Hello, World!'