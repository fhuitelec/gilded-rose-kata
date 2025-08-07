"""Test suite for the Gilded Rose inventory system."""

from gilded_rose.inn import GildedRose, Item


def test_foo():
    """Dummy test to ensure the test suite is working."""
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].name == "fixme"
