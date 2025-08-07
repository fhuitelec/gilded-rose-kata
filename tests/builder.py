"""Tests builder helpers to make tests' intention more obvious."""

from dataclasses import dataclass
from typing import Self

from gilded_rose.inn import Item

AGED_BRIE = "Aged Brie"


@dataclass
class ItemBuilder:
    """Builder to help creating Items."""

    ennobles: bool = False
    sell_date: int = 4
    quality: int = 5

    def with_quality(self, quality: int) -> Self:
        """Add a specific quality to the item to build."""
        self.quality = quality
        return self

    def expired(self) -> Self:
        """Mark the item as expired."""
        self.sell_date = 0
        return self

    def sell_in(self, sell_date: int) -> Self:
        """Add a specific sell-in date to the item to build."""
        self.sell_date = sell_date
        return self

    def ennobling(self) -> Self:
        """Markthe item to build as an article which ennobles over time."""
        self.ennobles = True
        return self

    def build(self) -> Item:
        """Build the Item object from the builder's characteristics."""
        name = AGED_BRIE if self.ennobles else "foo"

        return Item(name, sell_in=self.sell_date, quality=self.quality)


def an_item() -> ItemBuilder:
    """Helper to return an item builder."""
    return ItemBuilder()
