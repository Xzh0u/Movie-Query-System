import csv
from typing import Dict, List


# MovieItems:
# 根据输入条件进行计算，返回所需展示的电影条目
#
# 参数:
#        filename -- 获取数据的文件路径
#
# 返回:
#        展示的电影条目
class MovieItems(object):
    def __init__(self, filename: str):
        self.filename = filename

    # getTagedItems:
    # 返回所有特定分类的条目
    #
    # 参数:
    #        tag -- 用户选取的分类
    #
    # 返回:
    #        展示的电影条目
    def getTagedItems(self, tag: dict):  # dict: {tagname: tag}
        pass

    # getSortedItems:
    # 根据特定类别进行快速排序
    #
    # 参数:
    #        tag -- 用户选取的分类
    #
    # 返回:
    #        展示的电影条目
    def getSortedItems(self, sortItem: str) -> List[Dict[str, str]]:
        return items

    # getTypedItems:
    # 根据用户输入字符串返回展示的电影条目
    #
    # 参数:
    #        input -- 用户输入的字符串
    #
    # 返回:
    #        展示的电影条目
    def getTypedItems(self, input: str):
        pass

    # getAllItems：
    # 返回所有电影条目
    #
    # 参数:
    #        filename -- 获取数据的文件路径
    #
    # 返回:
    #        所有电影条目
    def getAllItems(self, filename: str):
        with open('Movies250.csv') as f:
            allItems = [{k: v
                         for k, v in row.items()}
                        for row in csv.DictReader(f, skipinitialspace=True)]
        # TODO: shuffle
        return allItems


if __name__ == "__main__":
    print(allMovieItems())