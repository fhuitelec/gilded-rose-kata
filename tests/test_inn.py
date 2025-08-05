"""Test suite for the golded rose inn package."""

import pytest

from gilded_rose.inn import GildedRose, Item

AGED_BRIE = "Aged Brie"


def test_sell_in_decreases_over_time():
    """Test items' sell-in date decreases over time."""
    # Arrange
    items = [
        Item("foo", sell_in=5, quality=3),
        Item("bar", sell_in=4, quality=3),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert len(items) == 2
    assert items[0].sell_in == 4
    assert items[1].sell_in == 3


def test_quality_degrades_over_time():
    """Test items' quality degrades over time."""
    # Arrange
    items = [
        Item("foo", sell_in=5, quality=3),
        Item("bar", sell_in=4, quality=3),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert len(items) == 2
    assert items[0].quality == 2
    assert items[1].quality == 2


def test_quality_cannot_get_degrades_twice_as_fast_when_item_is_expired():
    """Test items' quality degrades twice as fast when an item's sell-in date has passed."""
    # Arrange
    items = [
        Item("foo", sell_in=0, quality=3),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert len(items) == 1
    assert items[0].quality == 1


def test_quality_cannot_get_negative():
    """Test items' quality cannot become negative."""
    # Arrange
    items = [
        Item("foo", sell_in=2, quality=0),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 0


def test_aged_brie_ennobles_with_time():
    """Test aged bries' quality increases with time."""
    # Arrange
    items = [
        Item(AGED_BRIE, sell_in=2, quality=2),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 3


def test_aged_brie_ennobles_twice_as_fast_when_it_is_expired():
    """Test aged bries' quality increases twice as fast once the items' sell-in date has passed."""
    # Arrange
    items = [
        Item(AGED_BRIE, sell_in=0, quality=2),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 4


def test_quality_cannot_exceed_50():
    """Test items' quality cannot go over 50."""
    # Arrange
    items = [
        Item(AGED_BRIE, sell_in=1, quality=50),
    ]
    gilded_rose = GildedRose(items)

    # Act
    gilded_rose.update_quality()

    # Assert
    assert items[0].quality == 50


@pytest.mark.skip(reason="This behaviour has not been implemeted yet.")
def test_quality_cannot_exceed_50_when_instanciated():
    """Test items' quality cannot go over 50 at its creation."""
    # Arrange
    with pytest.raises(ValueError):
        Item(AGED_BRIE, sell_in=1, quality=50)
