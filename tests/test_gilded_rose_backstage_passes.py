from gilded_rose.gilded_rose import Item, update_quality
from tests.builders import BACKSTAGE_PASSES, given_an_item


def test_backstage_passes_ennobles_with_time():
    item = given_an_item().with_name(BACKSTAGE_PASSES).that_is_backstage().with_sell_date(20).with_quality(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 6


def test_backstage_passes_ennobles_twice_as_much_when_sell_date_is_less_than_10_days():
    item = given_an_item().with_name(BACKSTAGE_PASSES).that_is_backstage().with_sell_date(8).with_quality(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 7


def test_backstage_passes_ennobles_three_times_as_much_when_sell_date_is_less_than_5_days():
    item = given_an_item().with_name(BACKSTAGE_PASSES).that_is_backstage().with_sell_date(4).with_quality(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 8


def test_backstage_passes_quality_drops_to_zero_when_sell_date_has_passed():
    item = given_an_item().with_name(BACKSTAGE_PASSES).that_is_backstage().with_sell_date(-1).with_quality(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 0
