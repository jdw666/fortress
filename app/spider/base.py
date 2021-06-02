# coding: utf-8


import os
import requests
import platform
import random
import time
import re
import json
import configparser
from bs4 import BeautifulSoup
import pymysql
from lxml import etree
import jieba
import jieba.analyse


def timestamp():
    t = time.localtime(time.time())
    ty = str(t.tm_year)
    tm = str(t.tm_mon)
    td = str(t.tm_mday)
    th = str(t.tm_hour).zfill(2)
    tmi = str(t.tm_min).zfill(2)
    ut = str(ty + tm + td + "_" + th + tmi)
    return ut


def log(content, path, name=None):
    root = os.path.abspath(__file__)
    item = root.split("app")[0]
    LogPath = item + "runtime/spider/"+path
    file = ""
    if name is None:
        file = (timestamp()+ ".html")
        file = (timestamp() + ".html")
    else:
        file = name + "_" + timestamp()
    if not os.path.exists(LogPath):
        os.makedirs(LogPath)
    f = open(LogPath + file, "a", encoding="UTF-8")
    f.write(content)
    f.close()


def getSentence(subject, url):
    path = subject + "/"
    first_hrefs = gethref(path, url, url)
    i = 0
    urls = []
    for href in first_hrefs:
        try:
            second_hrefs = gethref(path, url, href)
        except:
            continue
        if href not in urls:
            urls.append(href)

            for second_href in second_hrefs:
                try:
                    third_hrefs = gethref(path, url, second_href)
                except:
                    continue
                if href not in urls:
                    urls.append(second_href)

            #         for third_href in third_hrefs:
            #             try:
            #                 forth_hrefs = gethref(path,url,third_href)
            #             except:
            #                 continue
            #             if href not in urls:
            #                 urls.append(third_href)


def gethref(path, master, href):
    response = requests.get(url=href)
    if 'utf-8' in response:
        response.encoding = "utf-8"
    elif "gbk" in response:
        response.encoding = "gbk"
    html = etree.HTML(response.text)
    urls = []
    i = 0
    name = re.sub(
        u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", href)
    hrefs = html.xpath('//a/@href')
    title = html.xpath('//h1/text()')
    sentence = html.xpath('//p/text()')
    log(str(response.text), "html/"+path, str(i)+name)
    if sentence and title:
        file = re.sub(
            u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", title[0])
        for item in sentence:
            log(item, 'sentence/'+path, file)
            log('\n', 'sentence/'+path, file)
    for link in hrefs:
        if "http" not in link:
            url = master + link
        else:
            url = link
        if url not in urls:
            urls.append(url)
        i += 1
    return urls


def getData(subject, kw1, kw2=None):
    path = "tmp/sentence/" + subject + "/"
    files = os.listdir(path)
    data = []
    for file in files:
        text = open(path + file, "r", encoding="UTF-8")
        str = text.read()
        item = str.split(kw1, 1)
        if kw2:
            try:
                item = item[1].split(kw2)
            except:
                continue
        text.close()
        if item[0]:
            log(item[0], 'vaild/'+subject, file)
            log('\n', 'vaild/'+subject, file)
            single = (file, 2, item[0], subject)
            data.append(single)
    sqlInsert(data)


def Publish():
    sentences = sqlfetch()
    for sentence in sentences:
        headers = {"Content-Type":"application/json"}
        url = "https://www.yixzm.cn/page/reading/contribute"
        keyword_list = jieba.analyse.textrank(sentence[3], topK=10)
        keywords = ''
        for keyword in keyword_list:
            keywords += keyword+','
        keywords = keywords[:-1]
        payload = {
            "title":sentence[1],
            "type":sentence[2],
            "content":sentence[3],
            "suffix":"html",
            "source_site":sentence[4],
            "keyword":keywords
        }
        data = json.dumps(payload)
        res = requests.post(url,data,headers)
        sqlUpdate(sentence[0],keywords)


def sqlLink():
    config = configparser.ConfigParser()
    root = os.path.abspath(__file__)
    item = root.split("app")[0]
    config.read(item + "env.ini")
    host = config.get("testing_mysql", "host")
    port = config.get("testing_mysql", "port")
    user = config.get("testing_mysql", "user")
    passwd = config.get("testing_mysql", "passwd")
    db = config.get("testing_mysql", "db")
    charset = config.get("testing_mysql", "charset")
    db = pymysql.connect(
        host=host,
        port=int(port),
        user=user,
        passwd=passwd,
        db=db,
        charset=charset)
    return db


def sqltruncate(table):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''truncate %s''' % (table)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def sqlInsert(data):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''INSERT INTO yi_index_articles(title, classify,content,domain)
    VALUES (%s, %s, %s,%s)'''
    try:
        cursor.executemany(sql, data)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def sqlfetch():
    db = sqlLink()
    cursor = db.cursor()
    data = []
    sql = '''SELECT * FROM yi_index_articles \
    WHERE status = %s order by rand() limit 3''' % (1)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            single = (row[0], row[1], row[4], row[8], row[20])
            data.append(single)
        db.commit()
    except:
        db.rollback()
    db.close()
    return data


def sqlUpdate(id,keywords):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''update yi_index_articles set status = "%s",keyword = "%s" where id = %s''' % (
        0, keywords, id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def sqlClear(keyword):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''select id,'''+keyword+''' from yi_index_articles where '''+keyword+''' in (select '''+keyword+''' from yi_index_articles group by '''+keyword+''' having count('''+keyword+''')>1)
and id not in(select min(id) from yi_index_articles group by '''+keyword+''' having count('''+keyword+''')>1);'''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for id,name in result:
            if id:
                sql = 'delete from yi_index_articles where id = %s'%id
                cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()
def addKeyword():
    db = sqlLink()
    cursor = db.cursor()
    sql = '''select id,content from yi_index_articles;'''
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for id,content in result:
            content = content.replace(r'\n','')
            keyword_list = jieba.analyse.textrank(content, topK=10)
            keywords = ''
            for keyword in keyword_list:
                keywords += keyword+','
            keywords = keywords[:-1]
            print(id)
            print(keywords)
            sqlUpdate(id,keywords)
                
        db.commit()
    except:
        db.rollback()
    db.close()

def cmd(name):
    status = []
    root = os.getcwd()
    item = root.split("app")[0]
    print(item)
    try:
        os.system('python  ' + item + 'app/testing/base/test/' + name + '.py')
        status.append(".")
    except:
        status.append("F")
    return status
