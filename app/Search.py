import csv  # 导入csv文件
from .algorithm.Sort import quickSort, dateSort  # 导入自己实现的算法


# MovieFactory:
# 根据输入条件进行计算，返回所需展示的电影条目
#
# 参数:
#        filename -- 获取数据的文件路径
#
# 返回:
#        展示的电影条目
class MovieFactory(object):
    def __init__(self, data):
        self.data = data
        # self.filename = "data/Movies250.csv"

    # getTagedItems:
    # 返回所有特定分类的条目
    #
    # 参数:
    #        tag -- 用户选取的分类
    #
    # 返回:
    #        展示的电影条目
    def getTagedItems(self, tag: dict):  # dict: {tagname: tag}
        rawItems = self.data
        items = []

        for i in range(len(rawItems)):
            for key in tag.keys():
                if key in rawItems[i]:
                    # 根据 key: tag 筛选
                    if type(rawItems[i][key]) == list:
                        for j in range(len(rawItems[i][key])):
                            if rawItems[i][key][j] == tag[key]:
                                items.append(rawItems[i])
                                break
                    elif type(rawItems[i][key]) == str:
                        if rawItems[i][key] == tag[key]:
                            items.append(rawItems[i])
                            break

        return items

    # getSortedItems:
    # 根据特定类别进行快速排序
    #
    # 参数:
    #        tag -- 用户选取的分类
    #
    # 返回:
    #        展示的电影条目
    def getSortedItems(self, sortItem: str):
        rawItems = self.data
        items = []
        sortedItems = []

        for i in range(len(rawItems)):
            if sortItem in rawItems[i]:
                selectItem = rawItems[i][sortItem]
                items.append(selectItem)

        if sortItem == 'date':  # 日期排序算法
            dateSort(items)

        if type(selectItem) == int or float:  # 数字排序算法
            quickSort(items, 0, len(items) - 1)

        # 输出排序后条目
        for i in range(len(rawItems)):
            for j in range(len(rawItems)):
                if rawItems[j][sortItem] == items[i]:
                    sortedItems.append(rawItems[j])

        return sortedItems

    # getTypedItems:
    # 根据用户输入字符串返回展示的电影条目
    #
    # 参数:
    #        input -- 用户输入的字符串
    #
    # 返回:
    #        展示的电影条目
    def getTypedItems(self, input: str):
        rawItems = self.data
        guess = []

        for i in range(len(rawItems)):
            for j in range(len(rawItems[i]["title"])):
                if input in rawItems[i]["title"][j]:
                    guess.append(rawItems[i]["title"][j])

        return guess

    # getAllItems：
    # 从文件中返回所有电影条目
    #
    # 参数:
    #        filename -- 获取数据的文件路径
    #
    # 返回:
    #        所有电影条目
    # TODO: to be modify, remeber to shuffle
    def getAllItems(self):
        with open(self.filename) as f:
            allItems = [{k: v
                         for k, v in row.items()}
                        for row in csv.DictReader(f, skipinitialspace=True)]
        return allItems


# parseAdaptation:
# 从introduction中解析是否有“改编”字样
#
# 参数:
#        data -- 输入数据
#
# 返回:
#        dict中增加一项 Adaptation: bool
def parseAdaptation(data):
    parseItem = "introduction"
    content = []
    adaptation = []
    for i in range(len(data)):
        if parseItem in data[i]:
            content.append(str(data[i][parseItem].split()))

    for i in range(len(content)):
        if "改编" in content[i]:
            adaptation.append(True)
        else:
            adaptation.append(False)

    # add a adaptation item
    for i in range(len(data)):
        data[i]["adaptation"] = adaptation[i]

    return data


if __name__ == "__main__":
    items = [{
        'rank': 2,
        'score': 9.6,
        'country': '中国大陆',
        'language': '汉语普通话',
        'director': '罗伯特·泽米吉斯',
        'major character': ['汤姆·汉克斯 Tom Hanks', 'xxx'],
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
        'major character': ['蒂姆·罗宾斯 Tim Robbins', 'xxx'],
        'title':
        ['肖申克的救赎', 'The Shawshank Redemption', '月黑高飞(港)', '刺激1995(台)'],
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
        'major character': ['蒂姆·罗宾斯 Tim Robbins'],
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
    items = MovieFactory(items)
    # print(items.getTypedItems('泰'))
    print(items.getSortedItems('date'))
    # tag = {'major character': 'xxx'}
    # print(items.getTagedItems(tag))

    # print(parseAdaptation(items))