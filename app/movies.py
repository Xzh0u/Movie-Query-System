from flask import (Blueprint, request, session)
from flask import jsonify
from flask_cors import CORS
from flask import Response
from .search import MovieFactory
import ast  # 用于string转dict

server = Blueprint('movies', __name__, url_prefix='/get_movies')
CORS(server)


def freeze(d):
    if isinstance(d, dict):
        return frozenset((key, freeze(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze(value) for value in d)
    return d


# 真正的items从文件读取，并且需要parseAdaptation
items = [{
    'rank': 2,
    'score': 9.6,
    'country': '中国大陆',
    'language': '汉语普通话',
    'director': '罗伯特·泽米吉斯',
    'majors': ['汤姆·汉克斯 Tom Hanks', 'xxx'],
    'title': ['霸王别姬', '再见，我的妾'],
    'type': ['爱情', '剧情'],
    'date': '1993-01-01',
    'introduction':
    '　段小楼（张丰毅）与程蝶衣（张国荣）是一对打小一起长大的师兄弟，两人一个演生，一个饰旦，一向配合天衣无缝，尤其一出《霸王别姬》，更是誉满京城，为此，两人约定合演一辈子《霸王别姬》。但两人对戏剧与人生关系的理解有本质不同，段小楼深知戏非人生，程蝶衣则是人戏不分。段小楼在认为该成家立业之时迎娶了名妓菊仙（巩俐），致使程蝶衣认定菊仙是可耻的第三者，使段小楼做了叛徒，自此，三人围绕一出《霸王别姬》生出的爱恨情仇战开始随着时代风云的变迁不断升级，终酿成悲剧。',
    'link': {
        '爱奇艺':
        'https://www.iqiyi.com/v_19rra0h3wg.html?vfm=m_331_dbdy&fv=4904d94982104144a1548dd9040df241',
        '腾讯视频':
        'https://v.qq.com/x/cover/1o29ui77e85grdr.html?ptag=douban.movie'
    }
}, {
    'rank':
    1,
    'score':
    9.7,
    'country':
    '美国',
    'language':
    '英语',
    'director':
    '弗兰克·德拉邦特',
    'majors': ['蒂姆·罗宾斯 Tim Robbins', 'xxx'],
    'title': ['肖申克的救赎', 'The Shawshank Redemption', '月黑高飞(港)', '刺激1995(台)'],
    'type': ['犯罪', '剧情'],
    'date':
    '1994-09-10',
    'introduction':
    '20世纪40年代末，小有成就的青年银行家安迪（蒂姆·罗宾斯 Tim Robbins 饰）因涉嫌杀害妻子及她的情人而锒铛入狱。在这座名为鲨堡的监狱内，希望似乎虚无缥缈，终身监禁的惩罚无疑注定了安迪接下来灰暗绝望的人生。未过多久，安迪尝试接近囚犯中颇有声望的瑞德（摩根·弗 里曼 Morgan Freeman 饰），请求对方帮自己搞来小锤子。以此为契机，二人逐渐熟稔，安迪也仿佛在鱼龙混杂、罪恶横生、黑白混淆的牢狱中找到属于自己的求生之道。他利用自身的专业知识，帮助监狱管理层逃税、洗黑钱，同时凭借与瑞德的交往在犯人中间也渐渐受到礼遇。表面看来，他已如瑞德那样对那堵高墙从憎恨转变为处之泰然，但是对自由的渴望仍促使他朝着心中的希望和目标前进。而关于其罪行的真相，似乎更使这一切朝前推进了一步……本片根据著名作家斯蒂芬·金（Stephen Edwin King）的原著改编。',
    'link': {
        '爱奇艺':
        'https://www.iqiyi.com/v_19rra0h3wg.html?vfm=m_331_dbdy&fv=4904d94982104144a1548dd9040df241',
        '腾讯视频':
        'https://v.qq.com/x/cover/1o29ui77e85grdr.html?ptag=douban.movie'
    }
}, {
    'rank': 5,
    'score': 9.2,
    'country': '美国',
    'language': '英语',
    'director': '詹姆斯·卡梅隆',
    'majors': ['蒂姆·罗宾斯 Tim Robbins'],
    'title': ['泰坦尼克号'],
    'type': ['爱情', '剧情', '灾难'],
    'date': '1998-04-03',
    'introduction':
    '1912年4月10日，号称 “世界工业史上的奇迹”的豪华客轮泰坦尼克号开始了自己的处女航，从英国的南安普顿出发驶往美国纽约。富家少女罗丝（凯特•温丝莱特）与母亲及未婚夫卡尔坐上了头等舱；另一边，放荡不羁的少年画家杰克（莱昂纳多·迪卡普里奥）也在码头的一场赌博中赢得了下等舱的船票。罗丝厌倦了上流社会虚伪的生活，不愿嫁给卡尔，打算投海自尽，被杰克救起。很快，美丽活泼的罗丝与英俊开朗的杰克相爱，杰克带罗丝参加下等舱的舞会、为她画像，二人的感情逐渐升温。1912年4月14日，星期天晚上，一个风平浪静的夜晚。泰坦尼克号撞上了冰山，“永不沉没的”泰坦尼克号面临沉船的命运，罗丝和杰克刚萌芽的爱情也将经历生死的考验。',
    'link': {
        '爱奇艺':
        'https://www.iqiyi.com/v_19rra0h3wg.html?vfm=m_331_dbdy&fv=4904d94982104144a1548dd9040df241',
        '腾讯视频':
        'https://v.qq.com/x/cover/1o29ui77e85grdr.html?ptag=douban.movie'
    }
}]


@server.route('/sorted_movies', methods=('GET', 'POST'))
def getSortedMovies():
    if request.method == 'GET':
        sortItem = request.args['sort_item']
        item = MovieFactory(items)
        movies = jsonify(item.getSortedItems(sortItem))
        return movies


@server.route('/taged_movies', methods=('GET', 'POST'))
def getTagedMovies():
    if request.method == 'GET':
        tag = ast.literal_eval(request.args['tag'])
        item = MovieFactory(items)
        movies = jsonify(item.getTagedItems(tag))
        return movies


@server.route('/typed_movies', methods=('GET', 'POST'))
def getTypedMovies():
    if request.method == 'GET':
        word = request.args['word']
        item = MovieFactory(items)
        movies = jsonify(item.getTypedItems(word))
        return movies


@server.route('/all_movies', methods=('GET', 'POST'))
def getAllMovies():
    return jsonify(items)