"""Test suite for the Gilded Rose inventory system."""

from gilded_rose.inn import GildedRose, Item
from tests.builder import an_item

AGED_BRIE = "Aged Brie"


def test_quality_degrades_over_time():
    """Test that the quality of an item decreases over time."""
    # Arrange
    items = [Item("foo", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)
    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 19


def test_sell_in_date_decreases_over_time():
    """Test that the sell-in date of an item decreases."""
    # Arrange
    items = [Item("foo", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].sell_in == 9


def test_quality_degrades_twice_as_fast_after_sell_in_date_is_passed():
    """Test that the quality of an item degrades twice as fast after the sell-in date."""
    # Arrange
    items = [Item("foo", sell_in=0, quality=20)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 18


def test_quality_cannot_get_negative():
    """Test that the quality of an item does not go below zero."""
    # Arrange
    items = [Item("foo", sell_in=10, quality=0)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 0


def test_aged_brie_ennobles_quality_over_time():
    """Test that the quality of Aged Brie increases over time."""
    # Arrange
    items = [Item(AGED_BRIE, sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 21


def test_quality_cannot_exceed_50():
    """Test that the quality of Aged Brie does not exceed 50."""
    # Arrange
    items = [an_item().ennobling().with_quality(50).build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 50


def test_ennobling_items_ennobles_twice_as_fast_after_sell_in_date_is_passed():
    """Test that the quality of Aged Brie increases twice as fast after the sell-in date has passed."""
    # Arrange
    items = [an_item().with_quality(20).ennobling().expired().build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 22


def test_legendary_never_sells_or_degrades():
    """Test that the sell-in date and quality of legendary items do not decrease."""
    # Arrange
    items = [an_item().legendary().build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 80
    assert items[0].sell_in == 0
