from flask import (Blueprint, request, session)
from flask import jsonify
from flask_cors import CORS
from flask import Response

server = Blueprint('movies', __name__, url_prefix='/get_movies')
CORS(server)


@server.route('/all_movies', methods=('GET', 'POST'))
def getAllMovies():
    pass


@server.route('/taged_movies', methods=('GET', 'POST'))
def getTagedMovies():
    pass


@server.route('/sorted_movies', methods=('GET', 'POST'))
def getSortedMovies():
    pass


@server.route('/typed_movies', methods=('GET', 'POST'))
def getTypedMovies():
    pass