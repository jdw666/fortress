# test_demo_sheet.py
# coding: utf-8


from utils import base
from lxml import etree
import time


db = base.proSqlLink()
cursor = db.cursor()
sql1 = '''update yi_security_sysdig x INNER JOIN yi_security_sysdig_info y ON x._pid = y.ppid and \
    x.sip = y.ip set valid = "%s" where x.valid = "%s" and x.time < DATE_SUB(NOW(), INTERVAL 1 hour)''' % (
    "true","todo")
sql2 = '''update yi_security_sysdig set valid = "%s" where valid = "%s" \
    and time < DATE_SUB(NOW(), INTERVAL 1 hour)''' % (
    "false","todo")
try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    results = cursor.fetchall()
    db.commit()
except:
    db.rollback()
db.close()
