from gilded_rose.gilded_rose import Item, GildedRose
from tests.builders import AGED_BRIE


def test_brie_ennobles_with_time():
    items = [Item(AGED_BRIE, sell_in=5, quality=2)]

    sut = GildedRose(items)
    sut.update_quality()

    assert items[0].quality == 3


def test_brie_ennobles_twice_as_much_when_sell_date_has_passed():
    items = [Item(AGED_BRIE, sell_in=0, quality=2)]

    sut = GildedRose(items)
    sut.update_quality()

    assert items[0].quality == 4
