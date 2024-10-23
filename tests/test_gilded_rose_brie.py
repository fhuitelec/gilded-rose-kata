from gilded_rose.gilded_rose import Item, update_quality
from tests.builders import AGED_BRIE, given_an_item


def test_brie_ennobles_with_time():
    item = given_an_item().with_name(AGED_BRIE).that_ennobles_with_time().with_quality(2).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 3


def test_brie_ennobles_twice_as_much_when_sell_date_has_passed():
    item = given_an_item().with_name(AGED_BRIE).that_ennobles_with_time().with_sell_date(0).with_quality(2).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 4
