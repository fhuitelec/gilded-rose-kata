import copy


def update_quality(items):
    new_items = []
    for old_item in items:
        item = copy.deepcopy(old_item)

        if item.name != "Aged Brie"\
            and item.name != "Backstage passes to a TAFKAL80ETC concert":
            new_items.append(item.age())

            continue

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


class Item:
    def __init__(self, name, ennobles, legendary, backstage, sell_in, quality):
        self.name = name
        self.ennobles = ennobles
        self.legendary = legendary
        self.backstage = backstage
        self.sell_in = sell_in
        self.quality = quality

    def age(self) -> "Item":
        quality_multiplier = 2 if self.sell_in <= 0 else 1

        sell_in = self.sell_in - 1
        quality = max(self.quality - quality_multiplier, 0)

        if self.ennobles:
            quality = min(self.quality + quality_multiplier, 50)

        if self.legendary:
            sell_in = self.sell_in
            quality = self.quality

        return Item(
            self.name,
            self.ennobles,
            self.legendary,
            self.backstage,
            sell_in,
            quality
        )

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
