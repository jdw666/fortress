def test_auto_TESTITEM_TAG_INDEX(self):
    responseText = base.getResponseText("URL")
    assert "KEYWORD" in responseText
