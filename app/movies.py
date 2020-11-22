from flask import (Blueprint, request, session)
from flask import jsonify
from flask_cors import CORS
from flask import Response
from .search import MovieProvider
from .get_frame import get_frames, get_img_stream
from .utils.utils import readMoviesCSV

server = Blueprint('movies', __name__, url_prefix='/movies')
CORS(server)


@server.route('')
def getMovies():
    items = readMoviesCSV()
    provider = MovieProvider(items)

    if request.args.get('adaptation') != None:
        adaptation = 'True' if request.args.get('adaptation') else 'False'
        items = provider.getTagedItems({'adaptation': adaptation})

    if request.args.get('major') != None:
        provider = MovieProvider(items)
        items = provider.getTagedItems({'majors': request.args.get('major')})

    tagType = ['country', 'type', 'director', 'language', 'title']
    for element in tagType:
        items = getTagMovies(items, element)

    # view sort not support now since no view count data
    if request.args.get('sort') != None and request.args.get('sort') != 'view':
        items = getSortMovies(items)

    # score needs to be float
    items = getSpecificScoreMovies(items)

    # 分页
    if request.args.get('limit') != None:
        limit = int(request.args.get('limit'))
        if request.args.get('offset') != None:
            offset = int(request.args.get('offset'))
        else:
            offset = 0
        items = items[0 + offset:limit + offset]

    return jsonify(items)


def getTagMovies(items, tagName):
    if request.args.get(tagName) != None:
        provider = MovieProvider(items)
        items = provider.getTagedItems({tagName: request.args.get(tagName)})

    return items


def getSortMovies(items):
    if request.args.get('sort') != None:
        provider = MovieProvider(items)
        items = provider.getSortedItems(request.args.get('sort'))

    return items


def getSpecificScoreMovies(items):
    if request.args.get('scoreSmallerThan') != None:
        movies = []
        for item in items:
            if item['score'] <= float(request.args.get('scoreSmallerThan')):
                movies.append(item)
        items = movies

    if request.args.get('scoreLargerThan') != None:
        movies = []
        for item in items:
            if item['score'] >= float(request.args.get('scoreLargerThan')):
                movies.append(item)
        items = movies

    if request.args.get('score') != None:
        movies = []
        for item in items:
            if item['score'] == float(request.args.get('score')):
                movies.append(item)
        items = movies

    return items


@server.route('/type/<string:typeName>')
def getMovieTypes(typeName):
    items = readMoviesCSV()
    provider = MovieProvider(items)

    typeNames = []
    for item in items:
        if type(item[typeName]) == list:
            for element in item[typeName]:
                typeNames.append(element)
        else:
            typeNames.append(item[typeName])
    typeNames = set(typeNames)
    typeNames = list(typeNames)

    return jsonify(typeNames)


@server.route('/images/<string:picName>', methods=('GET', 'POST'))
def getMovieImages():
    return jsonify(image=get_frames())