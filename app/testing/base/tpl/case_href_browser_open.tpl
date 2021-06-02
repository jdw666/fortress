def test_auto_TESTITEM_TAG_INDEX(self):
    responseText = base.browerOpen("URL")
    assert "KEYWORD" in responseText
