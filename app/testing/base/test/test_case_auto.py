# test_demo_sheet.py
# coding: utf-8


from utils import base
import requests
from lxml import etree



objects = ["'code_200'","'api_note'"]
for object in objects:
    items = base.sqlfetch(object)
    for item in items:
        id = item[0]
        url = item[3]
        try:
            if "test" in item[2]:
                url=url+":8000" 
            response = requests.get(url)
            code = str(response.status_code)
            assert "200" in code
            base.sqlUpdate(id,"pass")
        except:
            base.sqlUpdate(id,"error")
            continue
    
    
    
    
items = base.sqlfetch("'href_title'")
for item in items:
    id = item[0]
    url = item[3]
    kw = item[5]
    try:
        response = requests.get(url=url)
        response.encoding = "utf-8"
        html = etree.HTML(response.text)
        text = html.xpath('//head/title/text()')
        if text:
            title = text[0]
            title = title.replace("&", "&amp;")
            title = title.replace("“", "&ldquo;")
            title = title.replace("”", "&rdquo;")
            title = title.replace('"', "&quot;")
            assert kw in title
            base.sqlUpdate(id,"pass")
    except:
        base.sqlUpdate(id,"error")
        continue


base.sqlReport("'error'")
# base.sqltruncate("yi_index_test_report")