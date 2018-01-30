from family_finder import FamilyFinder
from json_source import data_v1


def test_can_get_ancestors():

    ff = FamilyFinder(data_v1)

    assert set(ff.getAncestors("Megan Holtz")) == set([
        "Billy Holtz",
        "Mickey Mouse",
        "Barbara Holtz",
        "Dina Dinkley",
        "Edwardo III",
        "Steve Long",
        "Sarah Long"
    ])
