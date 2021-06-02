# base.py
# coding: utf-8

import json
import os
import configparser
import platform
import random
import time





def log(content):
  job ="org.yixzm.cn" 
  logPath = ['/product/ai/connect.html','/product/ai/honeypot.html',
  '/product/ai/secid.html','/product/alyac_android',
  '/product/consultant/event.html','/product/consultant/law.html',
  '/product/ii/camera.html','/product/ii/dc.html']

  for route in logPath:
    list=route.split("/")
    file = list[-1]
    way = job+route.replace(file,"")
    # way=job+"".join(list.pop(-1))
    if not os.path.exists(way):
      os.makedirs(way)
    f = open(way+ file,"w+", encoding="UTF-8")
    f.write(content)
    f.close()

def buildHtml():
  str=open("php","r", encoding="UTF-8")
  php=str.read()
  log(php)


buildHtml()
