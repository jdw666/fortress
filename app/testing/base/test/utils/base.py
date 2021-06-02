# base.py
# coding: utf-8

import json
import os
import configparser
import requests
import platform
import random
import time
import re
import pymysql
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display


def getPath():
    root = os.path.abspath(__file__)
    item = root.split("app")[0]
    Path = item + "app/testing/base/"
    return Path


def env():
    config = configparser.ConfigParser()
    config.read("env.ini")
    target = config.get("mode", "target")
    host = config.get("host", target)
    return host


# def post(url, data, headers):
#     url = "http://" + env() + url
#     response = requests.post(url=url, json=data, headers=headers)
#     log(response.text)
#     return response.text


# def get(url, domain=None):
#     if domain == None:
#         domain = env()
#     url = "http://" + domain + url
#     response = requests.get(url=url)
#     return response.text


def code(url):
    response = requests.get(url)
    log("<!--" + url + "-->\n\n")
    log(response.text)
    code = str(response.status_code)
    return code


def getResponseText(url):
    response = requests.get(url=url)
    log(response.text)
    return response.text


def bhaviorModeling(driver):
    count = 0
    while count < 10:
        size = count * 0.1 + random.random() * 0.01
        script = "window.scrollTo(0, document.body.scrollHeight*" + \
            str(size) + ");"
        driver.execute_script(script)
        duration = random.randint(1, 3) + random.random()
        time.sleep(duration)
        count = count + random.randint(1, 2)


def browerOpen(url):
    if platform.system() == "Linux":
        display = Display(visible=0, size=(800, 800))
        display.start()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("window-size=1024,768")
        chrome_options.add_argument("--no-sandbox")
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome()
    driver.get(url=url)
    bhaviorModeling(driver)
    title = driver.title
    driver.quit()
    return title


def timestamp():
    t = time.localtime(time.time())
    ty = str(t.tm_year)
    tm = str(t.tm_mon)
    td = str(t.tm_mday)
    th = str(t.tm_hour).zfill(2)
    tmi = str(t.tm_min).zfill(2)
    ut = str(ty + tm + td + "_" + th + tmi)
    return ut


def logPath():
    root = os.path.abspath(__file__)
    item = root.split("app")[0]
    Path = item + "runtime/testing/"
    t = time.localtime(time.time())
    ty = str(t.tm_year)
    tm = str(t.tm_mon)
    td = str(t.tm_mday)
    th = str(t.tm_hour).zfill(2)
    tmi = str(t.tm_min).zfill(2)
    LP = str(Path+"log/" + ty + "." + tm + "/" + td + "/")
    return LP


def log(content, name=None):
    Timestamp = timestamp()
    LogPath = logPath()
    file = ""
    if name == None:
        file = Timestamp
    else:
        file = name + "_" + Timestamp
    if not os.path.exists(LogPath):
        os.makedirs(LogPath)
    f = open(LogPath + file, "a", encoding="UTF-8")
    f.write(content)
    f.close()


def createCaseCode200(protocal, domain, tag, url):
    host = protocal + "://" + domain
    url = host + url
    testItem = "code_200"
    data = []
    response = requests.get(url=url).text
    soup = BeautifulSoup(response, "html.parser")
    log(str(soup),testItem)
    links = []
    index = 0
    testcase = ""
    for item in soup.find_all("a"):
        link = item.get("href")
        if isinstance(link, str):
            if link not in links:
                links.append(link)
    links.sort()
    for item in links:
        if "http" not in item:
            newlink = host + item
        else:
            newlink = item
        single = (testItem, tag, newlink, '')
        data.append(single)
    sqlInsert(data)


def findRoute(index):
    table = []
    Path = getPath()
    php = open(Path + "tmp/sharp_spear/route/app.php", "r", encoding="utf-8")
    str = php.read()
    cases = str.split("case")
    routes = cases[index].split("('")
    for route in routes:
        interface = route.split("',")
        if "[" in interface[0]:
            newinterface = interface[0].split("/[")
            table.append(newinterface[0])
        else:
            table.append(interface[0])
    table.pop(0)
    return table


def createCaseApiNote(protocal, tag, url):
    Path = getPath()+"tmp/"
    url = protocal + url
    testItem = "api_note"
    root = os.getcwd()
    num = 1
    i = 0
    testcase = ""
    links = []
    link = []
    data = []
    newlinks = []
    domain = ['', '', 'www.dim5.cn', 'www.dim5.org', 'auth.yixzm.cn']
    job = Path + "sharp_spear/"
    directorys = ["chat", "dashboard", "demo",
                  "page", "qa", "sdk", "security", "shop"]
    if not os.path.exists(job):
        os.makedirs(Path)
        os.chdir(Path)
        cmd = "git clone git@code.yixzm.cn:ares/sharp_spear.git"
        os.system(cmd)
    else:
        os.chdir(job)
        cmd = "git pull & git checkout dev "
        os.system(cmd)
    os.chdir(root)
    for directory in directorys:
        logPath = job + "app/" + directory + "/controller/"
        files = os.listdir(logPath)
        for file in files:
            html = open(logPath + file, "r", encoding="utf-8")
            lines = html.readlines()
            for line in lines:
                if "@api" in line:
                    link = line.split()
                if 'public function' in line:
                    if len(link) > 1 and link[-1] not in links:
                        links.append(link[-1])
    while num < 4:
        num += 1
        routes = findRoute(num)
        for route in routes:
            index = 0
            while index + 1 < len(links):
                if links[index].find(route) == 1:
                    link = protocal + domain[num] + links[index]
                    links.pop(index)
                    if link not in newlinks:
                        newlinks.append(link)
                index += 1
    for item in links:
        if "pro" in tag:
            link = "https://www.yixzm.cn" + item
        else:
            link = protocal+"www.yixzm.cn" + item
        if link not in newlinks:
            newlinks.append(link)
    for newlink in newlinks:
        single = (testItem, tag, newlink, '')
        data.append(single)
    sqlInsert(data)


# api 筛选功能
def api_filtrate(name):
    Path = getPath()+"tmp/"
    job = Path + "sharp_spear/"
    directorys = ["chat", "dashboard", "demo", 
                  "page", "qa", "sdk", "security", "shop"]
    dict_s = {}
    for directory in directorys:
        logPath = job + "app/" + directory + "/controller/"
        files = os.listdir(logPath)
        for file in files:
            html = open(logPath + file, "r", encoding="utf-8")
            str_s = html.read()
            list1 = str_s.split("/**\n")
            list1[-1] = list1[-1][:-2]
            list1.pop(0)
            for x in list1:
                if "function" in x:
                    list2 = x.split("function")
                    if 'public' in list2[0]:
                        list2[0] = list2[0][0:-7]
                    if 'public' in list2[1]:
                        list2[1] = list2[1][0:-7]
                    if name in list2[0]:
                        dict_s["     /**\n" + list2[0]] = "public function" + list2[1]
    return dict_s


# js 筛选功能
def js_filtrate(name):
    print("来了老弟")
    Path = getPath()+"tmp/"
    job = Path + "sharp_spear/"
    dict_s = {}
    list_s = []
    name_list = []
    for filepath,dirnames,filenames in os.walk(job + 'public/c/master'):
        for filename in filenames:
            f_path = os.path.join(filepath,filename)
            if ".js" in f_path:
                file = open(f_path, "r", encoding="utf-8")
                file = file.read()
                if "methods" in file:
                    res = file.split("methods")
                    res.pop(0)
                    for x in res:
                        end = x.split("},")
                        end[0] = end[0][3:]
                        for i in end:
                            ret = re.match(r"\s*.*\(", i)
                            if ret:
                                try:
                                    if i[0:88] not in name_list:
                                        name_list.append(i[0:88])
                                        if name in ret.group():
                                            list_s.append(i)
                                except Exception as e:
                                        if name in ret.group():
                                            list_s.append(i)
    for x in range(len(list_s)):
        dict_s[x+1] = list_s[x] + "},"
    return dict_s


# model php 筛选
def php_filtrate(name):
    Path = getPath()+"tmp/"
    job = Path + "sharp_spear/"
    directorys = ["chat", "dashboard", "demo", 
                  "page", "qa", "sdk", "security", "shop"]
    dict_s = {}
    for directory in directorys:
        logPath = job + "app/" + directory + "/model/"
        try:
            files = os.listdir(logPath)
            for file in files:
                html = open(logPath + file, "r", encoding="utf-8")
                str_s = html.read()
                list1 = str_s.split("/**\n")
                list1[-1] = list1[-1][:-2]
                list1.pop(0)
                for x in list1:
                    if "function" in x:
                        list2 = x.split("function ")
                        if 'public' in list2[0]:
                            list2[0] = list2[0][0:-7]
                        if 'public' in list2[1]:
                            list2[1] = list2[1][0:-7]
                        if name in list2[0]:
                            dict_s["     /**\n" + list2[0]] = "public function" + list2[1]
        except Exception as e:
            pass
    return dict_s


# py 筛选功能
def py_filtrate(name):
    dict_s = {}
    # Path = getPath()
    Path = os.path.abspath(__file__)
    # print(Path, "----------")
    html = open(Path, "r", encoding="utf-8")
    str_s = html.read()
    list1 = str_s.split("def ")
    list1.pop(0)
    
    # print(list1)
    # for x in list1:
    #     if "function" in x:
    #         list2 = x.split("function")
    #         if 'public' in list2[0]:
    #             list2[0] = list2[0][0:-7]
    #         if 'public' in list2[1]:
    #             list2[1] = list2[1][0:-7]
    #         if name in list2[0]:
    #             dict_s["     /**\n" + list2[0]] = "public function" + list2[1]
    return dict_s   


def createCaseHrefTitle(protocal, domain, tag, url):
    host = protocal + "://" + domain
    url = host + url
    testItem = "href_title"
    response = requests.get(url=url).text
    html = etree.HTML(response)
    links = []
    data = []
    index = 0
    hrefs = []
    for item in html.xpath('//a'):
        href = item.get("href")
        title = item.get("title")
        if href:
            if href not in hrefs:
                hrefs.append(href)
                link = host + href
                if "http" in href:
                    link = href
                newlink = link
                kw = '空值'
                if title:
                    kw = title
                    kw = kw.replace("&", "&amp;")
                    kw = kw.replace("“", "&ldquo;")
                    kw = kw.replace("”", "&rdquo;")
                    kw = kw.replace('"', "&quot;")
                    kw = kw.replace('—', "&mdash;")
                single = (testItem, tag, newlink, kw)
                data.append(single)
    sqlInsert(data)


# 返回数组首个元素
def takeFirst(elem):
    return elem[0]


# 生成 selenium 在浏览器打开链接的用例
# @param domain 域名
# @param tag 用例标签
# @param url base链接
# @param kw 待判断关键字
def createCaseBrowserOpen(protocal, domain, tag, url):
    host = protocal + "://" + domain
    url = host + url
    testItem = "href_browser_open"
    response = requests.get(url=url).text
    soup = BeautifulSoup(response, "html.parser")
    links = []
    index = 0
    testcase = ""
    for item in soup.find_all("a"):
        href = item.get("href")
        title = item.get("title")
        link = (href, title)
        if isinstance(href, str):
            if link not in links:
                links.append(link)
    links.sort(key=takeFirst)
    for item in links:
        link = host + item[0]
        if "http" not in item[0]:
            url = link
        else:
            url = item[0]
        if item[1] != None:
            kw = item[1]
            kw = kw.replace("&", "&amp;")
            kw = kw.replace("“", "&ldquo;")
            kw = kw.replace("”", "&rdquo;")
            kw = kw.replace('"', "&quot;")


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
        host = host,
        port = int(port),
        user = user,
        passwd = passwd,
        db = db,
        charset = charset)
    return db

def proSqlLink():
    config = configparser.ConfigParser()
    root = os.path.abspath(__file__)
    item = root.split("app")[0]
    config.read(item + "env.ini")
    host = config.get("pro_mysql", "host")
    port = config.get("pro_mysql", "port")
    user = config.get("pro_mysql", "user")
    passwd = config.get("pro_mysql", "passwd")
    db = config.get("pro_mysql", "db")
    charset = config.get("pro_mysql", "charset")
    db = pymysql.connect(
        host = host,
        port = int(port),
        user = user,
        passwd = passwd,
        db = db,
        charset = charset)
    return db


def sqlInsert(data):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''INSERT INTO yi_index_test_case(classify,domain,url,keyword)
    VALUES (%s, %s, %s,%s)'''
    try:
        cursor.executemany(sql, data)
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


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


def sqlfetch(classify):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''SELECT * FROM yi_index_test_case \
    WHERE classify = %s''' % (classify)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.commit()
    except:
        db.rollback()
    db.close()
    return results


def sqlReport(status):
    db = sqlLink()
    cursor = db.cursor()
    domains = ("code_200", "api_note", "href_title")
    reports = []
    for domain in domains:
        classify = '"' + domain + '"'
        urls = []
        index = 0
        sql = '''SELECT * FROM yi_index_test_case \
        WHERE status = %s and classify = %s''' % (status, classify)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            for result in results:
                urls.append('\n'+result[3])
                report = (result[1], result[2], result[3],result[5])
                # log(result[3],"url")
                # log('\n',"url")
                reports.append(report)
                log(str(report),"report")
                log("\n","report")
                index += 1
            url = ','.join(urls)
            sql2 = '''INSERT INTO yi_index_test_report(classify,amount,url)
            VALUES ('%s', '%s', '%s')''' % (domain, index, url)
            if url:
                cursor.execute(sql2)
        except:
            db.rollback()
    db.close()
    # log(str(reports),"report")
    # log("\n","report")
    return reports


def sqlUpdate(id, content):
    db = sqlLink()
    cursor = db.cursor()
    sql = '''update yi_index_test_case set status = "%s" where id = %s''' % (
        content, id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()

def cmd(type,name):
    status = []
    if platform.system() == "Linux":
        type = type +"3"
    root = os.getcwd()
    item = root.split("app")[0]
    if "python" in type:
        path = item + '/app/testing/base/test/'
    elif "bash" in type:
        path = item + '/app/testing/base/script/'
    try:
        os.system(type + '  ' + path + name)
        status.append("success!")
    except:
        status.append("default!")
    return status