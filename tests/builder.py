"""Tests builder helpers to make tests' intention more obvious."""

from dataclasses import dataclass
from typing import Self

from gilded_rose.inn import Item

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"


@dataclass
class ItemBuilder:
    """Builder to help creating Items."""

    _ennobles: bool = False
    _is_legendary: bool = False
    _sell_in_date: int = 4
    _quality: int = 5

    def _name(self) -> str:
        """Compute the item's name depending on its characteristics."""
        if self._ennobles:
            return AGED_BRIE
        if self._is_legendary:
            return SULFURAS
        return "foo"

    def with_quality(self, quality: int) -> Self:
        """Add a specific quality to the item to build."""
        self._quality = quality
        return self

    def expired(self) -> Self:
        """Mark the item as expired."""
        self._sell_in_date = 0
        return self

    def sell_in(self, sell_date: int) -> Self:
        """Add a specific sell-in date to the item to build."""
        self._sell_in_date = sell_date
        return self

    def ennobling(self) -> Self:
        """Markthe item to build as an article which ennobles over time."""
        if self._is_legendary:
            raise CannotBeEnnoblingAndLegendaryError()

        self._ennobles = True
        return self

    def legendary(self) -> Self:
        """Markthe item to build as an article which ennobles over time."""
        if self._ennobles:
            raise CannotBeEnnoblingAndLegendaryError()

        self._is_legendary = True
        return self

    def build(self) -> Item:
        """Build the Item object from the builder's characteristics."""
        return Item(self._name(), sell_in=self._sell_in_date, quality=self._quality)


def an_item() -> ItemBuilder:
    """Helper to return an item builder."""
    return ItemBuilder()


class CannotBeEnnoblingAndLegendaryError(ValueError):
    """Error to raise when trying to create an item both legendary & ennobling."""

    def __init__(self):
        """Instantiate the exception."""
        super().__init__(
            "An item cannot ennoble with time and be legendary at the same time"
        )
