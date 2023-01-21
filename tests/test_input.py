import src.input as input


def test_text_input():
    text = input.text_input()
    assert len(text['text']) > 0


def test_text_input2():
    text = input.text_input()
    assert type(text['text']) == str


def test_get_document():
    """requires network connection to another
    container so will return an empty dict"""
    doc = input.get_document("18942")
    assert len(doc) == 0


def test_get_pageids_from_graph():
    """requires network connection to another
    container so will return an empty list"""
    pageids = input.get_pageids_from_graph()
    assert len(pageids) == 0


def test_get_entity_relations():
    """requires network connection to another
    container so will return an empty list"""
    relations = input.get_entity_relationship_from_graph()
    assert len(relations) == 0
