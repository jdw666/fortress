# coding: utf-8

import get_data


class TestClassGetQuestions:
    def test_get_questions_000(self):
        get_data.getQuestions("https://www.diyifanwen.com/kaoshizhuanti/ruanjianshitiku/")

    # def test_get_questions_001(self):   
    #     get_data.getQuestions("https://www.diyifanwen.com/kaoshizhuanti/ruanjianshitiku/index_2.html")