"""Main module that manages the Gilded Rose inventory system."""

import copy
from dataclasses import dataclass


def update_quality(items):  # pylint: disable=too-many-branches
    """Update the quality and sell-in values of items in the inventory."""
    new_items = []
    for old_item in items:  # pylint: disable=too-many-nested-blocks
        item = copy.deepcopy(old_item)
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


# Todo: make Item a frozen dataclass
@dataclass
class Item:  # pylint: disable=too-few-public-methods
    """Class representing an item in the Gilded Rose inventory."""

    name: str
    sell_in: int
    quality: int

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)  # pylint: disable=consider-using-f-string
