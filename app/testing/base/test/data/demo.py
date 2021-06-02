# demo.py
# coding: utf-8

import random


def zwyp(self, v=2):
    if v == 1:
        return v1(self)
    elif v == 2:
        return v2(self)
    else:
        return v2()


def v1(self):
    unit = "".join(random.sample("寻溯科技而乘天元行之", 2))
    informant = "".join(random.sample("张伟王芳秀英李娜", 2))
    date = "2020-%d" % (random.randint(1, 12)) + "-%d" % (random.randint(1, 28))
    name = "".join(random.sample("丽磊明赵峰斌", 2))
    id_no = "%d" % (random.randint(100000000000000000, 999999999999999999))
    city = random.choice(["中卫市"])
    area = random.choice(["沙坡头区", "中宁县", "海原县"])
    address = (
        "".join(random.sample("济南青岛淄博枣庄东营烟", 2))
        + "".join(random.sample("东南西北", 1))
        + "路%d" % (random.randint(1, 9999))
        + "号"
    )
    tel = "%d" % (random.randint(13100000000, 19999999999)) + ""
    symptom = random.choice(["发热", "乏力", "干咳", "抗病毒", "其他"])
    temperature = "%.1f" % (random.uniform(35, 42)) + ""
    drugs = random.sample("感冒清热柴黄藿香正气软伤风感宁", 3)
    manufactor = "".join(random.sample("明水匡达新喘宁散", 2)) + "制药"
    relationship = random.choice(["师徒", "亲子", "伙伴"])
    remarks = random.choice(["本地人", "外地人"])
    data = {
        "unit": unit,
        "informant": informant,
        "date": date,
        "name": name,
        "id_no": id_no,
        "city": city,
        "area": area,
        "address": address,
        "tel": tel,
        "symptom": symptom,
        "temperature": temperature,
        "drugs": drugs,
        "manufactor": manufactor,
        "relationship": relationship,
        "remarks": remarks,
        "kw": "zwyp",
        "wx_id": "~",
    }
    return data


def v2(self):
    unit = "".join(random.sample("寻溯科技而乘天元行之", 2))
    informant = "".join(random.sample("张伟王芳秀英李娜", 2))
    date = "2020-%d" % (random.randint(1, 12)) + "-%d" % (random.randint(1, 28))
    name = "".join(random.sample("丽磊明赵峰斌", 2))
    guardian = "".join(random.sample("张伟王芳秀英李娜", 2))
    sex = random.choice(["男", "女"])
    id_no = "%d" % (random.randint(100000000000000000, 999999999999999999))
    province = random.choice(["宁夏", "上海", "山东"])
    city = random.choice(["中卫市"])
    area = random.choice(["沙坡头区", "中宁县", "海原县"])
    street = "".join(random.sample("济南青岛淄营烟", 2))
    village = "".join(random.sample("博枣庄东营", 2))
    address = (
        "".join(random.sample("济南青岛淄博枣庄东营烟", 2))
        + "".join(random.sample("东南西北", 1))
        + "路%d" % (random.randint(1, 9999))
        + "号"
    )
    tel = "%d" % (random.randint(13100000000, 19999999999)) + ""
    symptom = random.choice(["发热", "乏力", "干咳", "抗病毒", "其他"])
    temperature = "%.1f" % (random.uniform(35, 42)) + ""
    drugs = random.sample("感冒清热柴黄藿香正气软伤风感宁", 3)
    manufactor = "".join(random.sample("明水匡达新喘宁散", 2)) + "制药"
    relationship = random.choice(["师徒", "亲子", "伙伴"])
    remarks = random.choice(["本地人", "外地人"])
    data = {
        "unit": unit,
        "informant": informant,
        "date": date,
        "name": name,
        "guardian": guardian,
        "sex": sex,
        "id_no": id_no,
        "province": province,
        "city": city,
        "area": area,
        "address": address,
        "tel": tel,
        "symptom": symptom,
        "temperature": temperature,
        "drugs": drugs,
        "manufactor": manufactor,
        "relationship": relationship,
        "remarks": remarks,
        "kw": "zwyp",
        "wx_id": "~",
    }
    return data
