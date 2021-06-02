# coding: utf-8

from utils import base
import requests


base.sqltruncate("yi_index_test_case")


base.createCaseCode200("https", "www.yixzm.cn", "pro_yblog_sitemap", "/sitemap/allse.html")

base.createCaseCode200("http", "www.dim5.cn", "pro_dim5_co", "/")

base.createCaseCode200("http", "anti-fraud.pro.yixzm.cn", "pro_anti_fraud", "/homepage")

# base.createCaseCode200("http", "test.www.yixzm.cn", "test_yblog_sitemap", "/sitemap/allse.html")

# base.createCaseCode200("http", "test.www.dim5.cn", "test_dim5_co", "/")

# base.createCaseCode200("http", "test.www.dim5.org", "test_dim5_org", "/")

# base.createCaseCode200("http", "test.anti-fraud.pro.yixzm.cn", "test_anti_fraud", "/")





# base.createCaseApiNote("http://test.", "test_sharp_spear", "/")

base.createCaseApiNote("http://dev.", "dev_sharp_spear", "/")

base.createCaseApiNote("http://", "pro_sharp_spear", "/")



base.createCaseHrefTitle("https", "www.yixzm.cn", "pro_yblog_sitemap", "/sitemap/allse.html")

base.createCaseHrefTitle("http", "www.dim5.cn", "pro_dim5_co", "/")

# base.createCaseHrefTitle("http", "test.www.yixzm.cn", "test_yblog_sitemap", "/sitemap/allse.html")

# base.createCaseHrefTitle("http", "test.www.dim5.cn", "test_dim5_co", "/")

# base.createCaseHrefTitle("http", "test.www.dim5.org", "test_dim5_org", "/")
