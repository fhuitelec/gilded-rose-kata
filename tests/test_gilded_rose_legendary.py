from gilded_rose.gilded_rose import Item, GildedRose
from tests.builders import given_an_item, SULFURAS


def test_legendary_items_sell_date_stays_the_same_with_time():
    # Arrange
    item = given_an_item().that_is_legendary().with_sell_date(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert item.sell_in == 5


def test_legendary_items_quality_stays_the_same_with_time():
    # Arrange
    item = given_an_item().that_is_legendary().with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert item.quality == 5
