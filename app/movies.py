from flask import (Blueprint, request, session)
from flask import jsonify
from flask_cors import CORS
from flask import Response
from .search import MovieProvider
import ast  # 用于string转dict
from csv import DictReader  # 导入csv文件
from .get_frame import get_frames

server = Blueprint('movies', __name__, url_prefix='/get_movies')
CORS(server)


def freeze(d):
    if isinstance(d, dict):
        return frozenset((key, freeze(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze(value) for value in d)
    return d


with open('app/data/list.csv', 'r') as read_obj:
    reader = DictReader(read_obj)
    items = list(reader)
    for i in range(len(items)):
        items[i]["director"] = items[i]["director"].strip('[').strip(
            ']').strip('\'').strip('\'')
        items[i]["score"] = float(items[i]["score"])
        items[i]["rank"] = int(items[i]["rank"])
        items[i]["runtime"] = items[i]["runtime"].strip('[').strip(']').strip(
            '\'').strip('\'')
        items[i]["image_url"] = items[i]["image_url"].strip('[').strip(
            ']').strip('\'').strip('\'')
        items[i]["link"] = ast.literal_eval(items[i]["link"])
        items[i]["introduction"] = ast.literal_eval(items[i]["introduction"])
        items[i]["majors"] = ast.literal_eval(items[i]["majors"])
        items[i]["type"] = ast.literal_eval(items[i]["type"])
    print(items[0])


@server.route('/sorted_movies', methods=('GET', 'POST'))
def getSortedMovies():
    if request.method == 'GET':
        sortItem = request.args['sort_item']
        item = MovieProvider(items)
        movies = jsonify(item.getSortedItems(sortItem))
        return movies


@server.route('/taged_movies', methods=('GET', 'POST'))
def getTagedMovies():
    if request.method == 'GET':
        tag = ast.literal_eval(request.args['tag'])
        item = MovieProvider(items)
        movies = jsonify(item.getTagedItems(tag))
        return movies


@server.route('/typed_movies', methods=('GET', 'POST'))
def getTypedMovies():
    if request.method == 'GET':
        word = request.args['word']
        item = MovieProvider(items)
        movies = jsonify(item.getTypedItems(word))
        return movies


@server.route('/all_movies', methods=('GET', 'POST'))
def getAllMovies():
    return jsonify(items)


@server.route('/images', methods=('GET', 'POST'))
def getMovieImages():
    return jsonify(get_frames())