"""Main module that manages the Gilded rose inn shop."""


class GildedRose:  # pylint: disable=too-few-public-methods
    """Handles the items lifecycles."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):  # pylint: disable=too-many-branches
        """Updates sell-in and quality depending on item characteristics"""
        for item in self.items:  # pylint: disable=too-many-nested-blocks
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


class Item:  # pylint: disable=too-few-public-methods
    """Hold an item characteristics"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (  # pylint: disable=consider-using-f-string
            self.name,
            self.sell_in,
            self.quality,
        )
