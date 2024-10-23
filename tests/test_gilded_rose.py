from gilded_rose.gilded_rose import Item, update_quality
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
        given_an_item().with_sell_date(3).build(),
        given_an_item().with_sell_date(2).build(),
    ]

    updated_items = update_quality(items)

    assert len(items) == 2
    assert updated_items[0].sell_in == 2
    assert updated_items[1].sell_in == 1


def test_quality_degrades_with_time():
    items = [
        given_an_item().with_quality(5).build(),
        given_an_item().with_quality(4).build(),
    ]

    updated_items = update_quality(items)

    assert len(updated_items) == 2
    assert updated_items[0].quality == 4
    assert updated_items[1].quality == 3


def test_quality_degrades_twice_as_much_when_sell_date_has_passed():
    item = given_an_item().with_sell_date(0).with_quality(5).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 3


def test_quality_cannot_get_negative():
    item = given_an_item().with_sell_date(5).with_quality(0).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 0


def test_an_item_quality_cannot_exceed_50_with_time():
    item = given_an_item().that_ennobles_with_time().with_quality(50).build()

    updated_items = update_quality([item])

    assert updated_items[0].quality == 50


@pytest.mark.skip(reason="the Item class does not check this behaviour for now")
def test_an_item_quality_cannot_exceed_50_when_declared():
    with pytest.raises(ValueError):
        given_an_item().with_quality(60).build()
