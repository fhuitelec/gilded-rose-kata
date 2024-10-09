from gilded_rose.gilded_rose import Item, GildedRose


AGED_BRIE = "Aged Brie"


def test_brie_ennobles_with_time():
    # Arrange
    items = [Item(AGED_BRIE, sell_in=5, quality=2)]

    # Act
    sut = GildedRose(items)
    sut.update_quality()

    # Assert
    assert items[0].quality == 3


def test_brie_ennobles_twice_as_much_when_sell_date_has_passed():
    # Arrange
    items = [Item(AGED_BRIE, sell_in=0, quality=2)]

    # Act
    sut = GildedRose(items)
    sut.update_quality()

    # Assert
    assert items[0].quality == 4

# What happens if an item is >50 when being constructed?
