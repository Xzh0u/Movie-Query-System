header_str = '''
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: no-cache
Connection: keep-alive
Cookie: bid=JfoKOZGZ_mE; ll="108198"; __utmc=30149280; _vwo_uuid_v2=DBBEB1BE534DF7CE898728070150D4A7A|f26e466096a4d534ef2f30106e07d32a; __utmz=30149280.1597976838.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); dbcl2="196213190:Fcvkn3Ca8uk"; ck=B7e-; push_noty_num=0; push_doumail_num=0; __utmv=30149280.19621; __utmc=223695111; __utmz=223695111.1598954962.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1599048875%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.100001.4cf6=ac66ced586cded9e.1598954963.2.1599048875.1598956986.; _pk_ses.100001.4cf6=*; __utma=30149280.1449485767.1594461454.1598954895.1599048875.4; __utmb=30149280.0.10.1599048875; __utma=223695111.597016680.1598954962.1598954962.1599048875.2; __utmb=223695111.0.10.1599048875; ap_v=0,6.0
Host: movie.douban.com
Pragma: no-cache
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
'''


#字符串转dict
def str2dict(s, s1=';', s2='='):
    li = s.split(s1)
    res = {}
    for kv in li:
        li2 = kv.split(s2)
        if len(li2) > 1:
            li2[0] = li2[0].replace(':', '')
            res[li2[0]] = li2[1]
    return res


headers = str2dict(header_str, '\n', ': ')
if 'Content-Length' in headers:
    del headers['Content-Length']
    # print(headers)

import requests as req
from bs4 import BeautifulSoup


def readOnePage(n):
    headers['accept-encoding'] = 'gzip'
    r = req.get('https://movie.douban.com/top250?start=' + str(n * 25),
                headers=headers)
    soup = BeautifulSoup(r.text)
    items = soup.find_all('div', class_='item')
    return items


# print(readOnePage(1))

allitems = []
for i in range(10):
    allitems += readOnePage(i)
# print(allitems[2])

import re
import unicodedata


def getinfo(item):
    txt = item.find('div', class_='bd').find('p').text
    info = {
        'title':
        item.find('div', class_='hd').find('a').text,
        'director':
        re.compile("导演:\\s(.*_?)[\xa0\.\.\.]").findall(txt)[0].replace(
            '导演:', '').split(' ')[0],
        'major character':
        re.compile("主演:\\s(.*_?)[\xa0\.\.\.]").findall(txt)[0].replace(
            '主演:', '') if
        len(re.compile("主演:\\s(.*_?)[\xa0\.\.\.]").findall(txt)) > 0 else ' ',
        'year':
        txt.split('\n')[2].split('/')[0],
        'country':
        txt.split('\n')[2].split('/')[1],
        'type':
        txt.split('\n')[2].split('/')[2]
    }
    for k in info:
        info[k] = unicodedata.normalize("NFKD",
                                        info[k]).strip().replace('\n', '')
    return info


movies = []
for i in range(len(allitems)):
    movies.append(getinfo(allitems[i]))

import pandas as pd
df = pd.DataFrame.from_dict(movies)
df.to_csv('Movies250.csv')
print(df)
