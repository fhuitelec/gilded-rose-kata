"""Tests builder helpers to make tests' intention more obvious."""

from dataclasses import dataclass
from typing import Self

from gilded_rose.inn import AGED_BRIE, BACKSTAGE_PASSES, CONJURED_PREFIX, SULFURAS, Item


@dataclass
class ItemBuilder:
    """Builder to help creating Items."""

    _ennobles: bool = False
    _is_legendary: bool = False
    _is_backstage_passes: bool = False
    _sell_in_date: int = 4
    _quality: int = 5
    _conjured: bool = False

    def _name(self) -> str:
        """Compute the item's name depending on its characteristics."""
        prefix = CONJURED_PREFIX if self._conjured else ""
        if self._ennobles:
            return prefix + AGED_BRIE
        if self._is_legendary:
            return prefix + SULFURAS
        if self._is_backstage_passes:
            return prefix + BACKSTAGE_PASSES
        return prefix + "foo"

    def with_quality(self, quality: int) -> Self:
        """Add a specific quality to the item to build."""
        self._quality = quality
        return self

    def conjured(self) -> Self:
        """Mark the item to build as a conjured item."""
        self._conjured = True
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
        if self._is_legendary or self._is_backstage_passes:
            raise InconsistentCharacteristicsError()

        self._ennobles = True
        return self

    def legendary(self) -> Self:
        """Markthe item to build as an article which ennobles over time."""
        if self._ennobles or self._is_backstage_passes:
            raise InconsistentCharacteristicsError()

        self._is_legendary = True
        self._quality = 80
        self._sell_in_date = 0
        return self

    def backstage_passes(self) -> Self:
        """Mark the item to build as a Backstage Pass."""
        if self._ennobles or self._is_legendary:
            raise InconsistentCharacteristicsError()

        self._is_backstage_passes = True
        return self

    def build(self) -> Item:
        """Build the Item object from the builder's characteristics."""
        return Item(self._name(), sell_in=self._sell_in_date, quality=self._quality)


def an_item() -> ItemBuilder:
    """Helper to return an item builder."""
    return ItemBuilder()


class InconsistentCharacteristicsError(ValueError):
    """Error to raise when trying to create an item with inconsistent characteristics."""

    def __init__(self):
        """Instantiate the exception."""
        super().__init__(
            "An item cannot ennoble with time, legendary or backstage passes at the same time"
        )
