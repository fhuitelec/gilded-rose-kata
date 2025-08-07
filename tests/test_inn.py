"""Test suite for the Gilded Rose inventory system."""

from gilded_rose.inn import GildedRose, Item
from tests.builder import an_item


def test_quality_degrades_over_time():
    """Test that the quality of an item decreases over time."""
    # Arrange
    items = [Item("foo", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)
    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 19


def test_sell_in_date_decreases_over_time():
    """Test that the sell-in date of an item decreases."""
    # Arrange
    items = [Item("foo", sell_in=10, quality=20)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].sell_in == 9


def test_quality_degrades_twice_as_fast_after_sell_in_date_is_passed():
    """Test that the quality of an item degrades twice as fast after the sell-in date."""
    # Arrange
    items = [Item("foo", sell_in=0, quality=20)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 18


def test_quality_cannot_get_negative():
    """Test that the quality of an item does not go below zero."""
    # Arrange
    items = [Item("foo", sell_in=10, quality=0)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 0


def test_aged_brie_ennobles_quality_over_time():
    """Test that the quality of Aged Brie increases over time."""
    # Arrange
    items = [an_item().ennobling().sell_in(10).with_quality(20).build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 21


def test_quality_cannot_exceed_50():
    """Test that the quality of Aged Brie does not exceed 50."""
    # Arrange
    items = [an_item().ennobling().with_quality(50).build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 50


def test_ennobling_items_ennobles_twice_as_fast_after_sell_in_date_is_passed():
    """Test that the quality of Aged Brie increases twice as fast after the sell-in date has passed."""
    # Arrange
    items = [an_item().with_quality(20).ennobling().expired().build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 22


def test_legendary_never_sells_or_degrades():
    """Test that the sell-in date and quality of legendary items do not decrease."""
    # Arrange
    items = [an_item().legendary().build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 80
    assert gilded_rose.items[0].sell_in == 0


def test_backstage_passes_ennobles_with_time():
    """Test that the quality of Backstage Passes increases over time."""
    # Arrange
    item = an_item().backstage_passes().sell_in(20).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert sut.items[0].quality == 6


def test_backstage_passes_ennobles_twice_as_much_when_sell_date_is_less_than_10_days():
    """Test that the quality of Backstage Passes increases twice as much when the sell date is less than 10 days."""
    # Arrange
    item = an_item().backstage_passes().sell_in(8).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert sut.items[0].quality == 7


def test_backstage_passes_ennobles_three_times_as_much_when_sell_date_is_less_than_5_days():
    """Test that the quality of Backstage Passes increases three times as much when the sell date is less than 5 days."""
    # Arrange
    item = an_item().backstage_passes().sell_in(4).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert sut.items[0].quality == 8


def test_backstage_passes_quality_drops_to_zero_when_sell_date_has_passed():
    """Test that the quality of Backstage Passes drops to zero when the sell date has passed."""
    # Arrange
    item = an_item().backstage_passes().sell_in(0).with_quality(5).build()

    # Act
    sut = GildedRose([item])
    sut.update_quality()

    # Assert
    assert sut.items[0].quality == 0


def test_conjured_items_degrade_twice_as_fast():
    """Test that the quality of conjured items degrades twice as fast."""
    # Arrange
    items = [Item("Conjured Mana Cake", sell_in=3, quality=6)]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 4


def test_conjured_items_degrade_4_times_as_fast_after_sell_in_date_is_passed():
    """Test that the quality of conjured items degrades four times as fast after the sell-in date."""
    # Arrange
    items = [an_item().conjured().expired().with_quality(6).build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 2


def test_conjured_ennobling_items_ennobles_twice_as_fast():
    """Test that conjured ennobling items increase quality twice as fast."""
    # Arrange
    items = [an_item().conjured().ennobling().sell_in(10).with_quality(20).build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 22


def test_conjured_ennobling_items_ennobles_four_times_as_fast_after_sell_in_date_is_passed():
    """Test that conjured ennobling items increase quality four times as fast after the sell-in date."""
    # Arrange
    items = [an_item().conjured().ennobling().expired().with_quality(20).build()]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert gilded_rose.items[0].quality == 24
