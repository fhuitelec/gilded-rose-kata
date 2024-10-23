from gilded_rose.gilded_rose import Item, update_quality
from tests.builders import given_an_item, SULFURAS


def test_legendary_items_sell_date_stays_the_same_with_time():
    item = given_an_item().that_is_legendary().with_sell_date(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].sell_in == 5


def test_legendary_items_quality_stays_the_same_with_time():
    item = given_an_item().that_is_legendary().with_quality(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 5
