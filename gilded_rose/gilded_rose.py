import copy


def update_quality(items):
    return [item.age() for item in items]


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

        if self.backstage:
            quality = min(self.quality + 1, 50)
            if self.sell_in <= 10:
                quality = min(self.quality + 2, 50)
            if self.sell_in <= 5:
                quality = min(self.quality + 3, 50)

            if self.sell_in <= 0:
                quality = 0

        return Item(self.name, self.ennobles, self.legendary, self.backstage, sell_in, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
