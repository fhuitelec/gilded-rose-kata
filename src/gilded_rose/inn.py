"""Main module that manages the Gilded Rose inventory system."""

from dataclasses import dataclass

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"


@dataclass(frozen=True)
class Item:  # pylint: disable=too-few-public-methods
    """Class representing an item in the Gilded Rose inventory."""

    name: str
    sell_in: int
    quality: int

    @property
    def _ennobling(self):
        """Returns whether the item ennobles over time."""
        return self.name == AGED_BRIE

    @property
    def _legendary(self):
        """Returns whether the item is legendary or not."""
        return self.name == SULFURAS

    @property
    def _backstage_passes(self):
        """Returns whether the item is a backstage pass or not."""
        return self.name == BACKSTAGE_PASSES

    def compute_after_a_day(self) -> "Item":
        """Compute the state of the item after a day."""
        quality_variation = 1 if self.sell_in > 0 else 2

        quality = max(0, self.quality - quality_variation)
        sell_in = self.sell_in - 1

        if self._ennobling:
            quality = min(50, self.quality + quality_variation)

        if self._legendary:
            quality = 80
            sell_in = self.sell_in

        if self._backstage_passes:
            quality = min(50, self.quality + 1)

        if self._backstage_passes and self.sell_in <= 10:
            quality = min(50, self.quality + 2)

        if self._backstage_passes and self.sell_in <= 5:
            quality = min(50, self.quality + 3)

        if self._backstage_passes and self.sell_in <= 0:
            quality = 0

        return Item(self.name, sell_in=sell_in, quality=quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)  # pylint: disable=consider-using-f-string


def update_quality(items: list[Item]):  # pylint: disable=too-many-branches
    """Update the quality and sell-in values of items in the inventory."""
    return [item.compute_after_a_day() for item in items]


class GildedRose:  # pylint: disable=too-few-public-methods
    """Class representing the Gilded Rose inventory system."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update the quality of items in the inventory."""
        self.items = update_quality(self.items)
