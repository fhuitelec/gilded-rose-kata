from gilded_rose.gilded_rose import Item, GildedRose
from tests.builders import AGED_BRIE, given_an_item


def test_brie_ennobles_with_time():
    item = given_an_item().with_name(AGED_BRIE).with_quality(2).build()

    sut = GildedRose([item])
    sut.update_quality()

    assert item.quality == 3


def test_brie_ennobles_twice_as_much_when_sell_date_has_passed():
    item = given_an_item().with_name(AGED_BRIE).with_sell_date(0).with_quality(2).build()

    sut = GildedRose([item])
    sut.update_quality()

    assert item.quality == 4