"""Main module that manages the Gilded Rose inventory system."""

import copy
from dataclasses import dataclass

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"


@dataclass
class Item:  # pylint: disable=too-few-public-methods
    """Class representing an item in the Gilded Rose inventory.

    Todo: make Item a frozen dataclass
    """

    name: str
    sell_in: int
    quality: int

    def _ennobling(self):
        """Returns whether the item ennobles over time."""
        return self.name == AGED_BRIE

    def _legendary(self):
        """Returns whether the item is legendary or not."""
        return self.name == SULFURAS

    def _backstage_passes(self):
        """Returns whether the item is a backstage pass or not."""
        return self.name == BACKSTAGE_PASSES

    def compute_after_a_day(self) -> "Item":
        """Compute the state of the item after a day."""
        quality_decrease = 1 if self.sell_in > 0 else 2

        quality = max(0, self.quality - quality_decrease)

        return Item(self.name, sell_in=self.sell_in - 1, quality=quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)  # pylint: disable=consider-using-f-string


def update_quality(items: list[Item]):  # pylint: disable=too-many-branches
    """Update the quality and sell-in values of items in the inventory."""
    new_items = []
    for old_item in items:  # pylint: disable=too-many-nested-blocks
        item = copy.deepcopy(old_item)

        if item.name not in (AGED_BRIE, BACKSTAGE_PASSES, SULFURAS):
            new_items.append(item.compute_after_a_day())
            continue

        if (
            item.name != "Aged Brie"  # pylint: disable=consider-using-in
            and item.name != "Backstage passes to a TAFKAL80ETC concert"
        ):
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        if item.name != "Sulfuras, Hand of Ragnaros":
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
        new_items.append(item)

    return new_items


class GildedRose:  # pylint: disable=too-few-public-methods
    """Class representing the Gilded Rose inventory system."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update the quality of items in the inventory."""
        self.items = update_quality(self.items)
