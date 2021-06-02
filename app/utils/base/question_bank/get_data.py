# coding: utf-8


import os
import requests
import platform
import random
import time
import re
from bs4 import BeautifulSoup
import pymysql
 





def log(content,name):
    LogPath = "question_bank/questions/"
    file = name 
    if not os.path.exists(LogPath):
        os.makedirs(LogPath)
    f = open(LogPath + file, "a", encoding="UTF-8")
    f.write(content)
    f.close()


def getQuestions(url):
    # testItem = "href"
    # response = requests.get(url=url)
    # response.encoding = "gbk"
    # soup = BeautifulSoup(response.text, "html.parser")
    # links = []
    # index = 0
    # files = []
    # for item in soup.find_all("a"):
    #     href = item.get("href")
    #     title = item.get("title")
    #     link = (href, title)
    #     if isinstance(href, str):
    #         if link not in links:
    #             links.append(link)
    # links.sort()
    # for link in links:
    #     index +=1
    #     if link[1] != None:
    #         url = "https:" + link[0]
    #         response = requests.get(url=url)
    #         response.encoding = "gbk"
    #         if "<br>" in str(response.text):
    #             items = str(response.text).split("<br>")
    #             for item in items:
    #                 data = item.split("<")
    #                 data[0].replace('&nbsp;','')
    #                 data[0].replace('&#8230;','')
    #                 if data[0] not in link[1]:
    #                     log(data[0],link[1])
    #                     log("\n",link[1])
    #                 files.append(link[1])
    sqlInsert('@全国软考程序员考试部分例题')
    


def sqlInsert(file):
    index = 0
    path = 'question_bank/questions/'+file 
    text = open(path, "r", encoding="UTF-8")
    file = text.read()
    lines = file.split("●")
    while index < 20:
        item = lines[index].split("@")
        index +=1
        question = item[0]
        options = item[1].split("解答：")
        option = options[0]
        if options != 1:
            answers = options[1].split("点评：")
            answer = answers[0]
            info = answers[1]
        
        # log(question,"question")
        # log("\n","question")
        # log(option,"option")
        # log("\n","option")
        # log(answer,"answer")
        # log("\n","answer")
        # log(info,"info")
        # log("\n","info")
        # index += 1
        # answer =""
        
        # data = datas.split('*')
        # for sth in data:
        #     answers = sth.split(") ")
        #     if "("+answers[0]+")" in question:
        #         one = answers[0] +'. '+ answers[1]
        #         answer=answer+


        db = pymysql.connect(
            host = '42.192.67.48',
            port = 3306,
            user = 'xsdber',
            passwd = '@163.com',
            db = 'test_db_yix_blog',
            charset = 'utf8')
        cursor = db.cursor()
        try:
            sql = '''INSERT INTO yi_qa_computer(question, option, answer, info, label)
            VALUES ('%s', '%s', '%s','%s','%s')'''%\
            (question, option, answer, info, '')
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        db.close()
