from gilded_rose.gilded_rose import Item, GildedRose
from tests.builders import BACKSTAGE_PASSES, given_an_item


def test_backstage_passes_ennobles_with_time():
    # Arrange
    item = given_an_item().with_name(BACKSTAGE_PASSES).with_sell_date(20).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert item.quality == 6


def test_backstage_passes_ennobles_twice_as_much_when_sell_date_is_less_than_10_days():
    # Arrange
    item = given_an_item().with_name(BACKSTAGE_PASSES).with_sell_date(8).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert item.quality == 7


def test_backstage_passes_ennobles_three_times_as_much_when_sell_date_is_less_than_5_days():
    # Arrange
    item = given_an_item().with_name(BACKSTAGE_PASSES).with_sell_date(4).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert item.quality == 8


def test_backstage_passes_quality_drops_to_zero_when_sell_date_has_passed():
    # Arrange
    item = given_an_item().with_name(BACKSTAGE_PASSES).with_sell_date(-1).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert item.quality == 0
