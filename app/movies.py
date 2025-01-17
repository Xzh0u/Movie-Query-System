from flask import (Blueprint, request, session)
from flask import jsonify
from flask_cors import CORS
from flask import Response
from .search import MovieProvider
from .get_frame import get_frames, get_img_stream
from .utils.utils import readMoviesCSV
from pandas import read_csv
from datetime import datetime

server = Blueprint('movies', __name__, url_prefix='/movies')
CORS(server)


@server.route('')
def getMovies():
    items = readMoviesCSV()
    provider = MovieProvider(items)
    items = provider.getSortedItems('score')

    if request.args.get('adaptation') != None:
        adaptation = 'True' if int(
            request.args.get('adaptation')) == 1 else 'False'
        items = provider.getTagedItems({'adaptation': adaptation})

    if request.args.get('major') != None:
        provider = MovieProvider(items)
        items = provider.getTagedItems({'majors': request.args.get('major')})

    tagType = ['country', 'type', 'director', 'language', 'title']
    for element in tagType:
        items = getTagMovies(items, element)

    if request.args.get('sort') != None:
        items = getSortMovies(items)

    items = getSpecificScoreMovies(items)

    count = len(items)
    # 分页
    if request.args.get('limit') != None:
        limit = int(request.args.get('limit'))
        if request.args.get('offset') != None:
            offset = int(request.args.get('offset'))
        else:
            offset = 0
        items = items[0 + offset:limit + offset]

    return jsonify({'movies': items, 'count': count})


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

    if typeName == 'major':
        typeName = 'majors'
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
def getMovieImages(picName):
    return jsonify(image=get_img_stream(picName))


@server.route('/click/<int:rank>', methods=('GET', 'POST'))
def addClickCount(rank):
    df = read_csv('app/data/list.csv')
    df.loc[df['rank'] == rank, ('view')] += 1
    df.to_csv('app/data/list.csv', index=False)
    return 'Successfully add 1'


@server.route('/comments/<int:rank>/<string:author>/<string:content>',
              methods=('GET', 'POST'))
def addComment(rank, author, content):
    df = read_csv(f'app/data/comments/{rank}.csv')
    comment = {
        'createdAt': datetime.now().timestamp(),
        'author': author,
        'content': content,
        'ip': request.remote_addr
    }
    df = df.append(comment, ignore_index=True)
    df.to_csv(f'app/data/comments/{rank}.csv', index=False)
    return 'Successfully add comment'


# return all comments of one movie
@server.route('/comments/<int:rank>', methods=('GET', 'POST'))
def loadComment(rank):
    df = read_csv(f'app/data/comments/{rank}.csv')
    comments = df.to_dict('records')
    return jsonify(comments)