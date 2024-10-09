from gilded_rose.gilded_rose import Item, GildedRose
from tests.builders import given_an_item
import pytest


# Notes:
# - one test per behaviour
#   - I initially had one test which tested quality & sell-in simultaneously
#   - degrade antonym
# - use the exact same terminology from the requirement (degrades, etc.)
# - builder for the quality cannot exceed 50 because it's tightly coupled to Aged Brie or equivalent

def test_sell_date_decreases_with_time():
    items = [
        Item("foo", sell_in=3, quality=5),
        Item("foo", sell_in=2, quality=4),
    ]

    sut = GildedRose(items)
    sut.update_quality()

    assert len(items) == 2
    assert items[0].sell_in == 2
    assert items[1].sell_in == 1


def test_quality_degrades_with_time():
    items = [
        Item("foo", sell_in=3, quality=5),
        Item("foo", sell_in=2, quality=4),
    ]

    sut = GildedRose(items)
    sut.update_quality()

    assert len(items) == 2
    assert items[0].quality == 4
    assert items[1].quality == 3


def test_quality_degrades_twice_as_much_when_sell_date_has_passed():
    items = [Item("foo", sell_in=0, quality=5)]

    sut = GildedRose(items)
    sut.update_quality()

    assert items[0].quality == 3


def test_quality_cannot_get_negative():
    items = [Item("foo", sell_in=5, quality=0)]

    sut = GildedRose(items)
    sut.update_quality()

    assert items[0].quality == 0


def test_an_item_quality_cannot_exceed_50_with_time():
    item = given_an_item().that_ennobles_with_time().with_quality(50).build()

    sut = GildedRose([item])
    sut.update_quality()

    assert item.quality == 50


@pytest.mark.skip(reason="the Item class does not check this behaviour for now")
def test_an_item_quality_cannot_exceed_50_when_declared():
    with pytest.raises(ValueError):
        given_an_item().with_quality(60).build()
