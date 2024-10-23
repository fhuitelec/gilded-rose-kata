from gilded_rose.gilded_rose import Item, QualityStrategy, SellStrategy

class ClassicStrategy(QualityStrategy):
    def get_quality(self, item: Item):
        if item.sell_in <= 0:
            return item.quality - 2

        return item.quality - 1


class BonnifyingStrategy(QualityStrategy):
    def get_quality(self, item: Item):
        if item.sell_in <= 0:
            return item.quality + 2

        return item.quality + 1


class BackstagePassStrategy(QualityStrategy):
    def get_quality(self, item: Item):
        if item.sell_in <= 0:
            return 0
        if item.sell_in <= 5:
            return item.quality + 3
        if item.sell_in <= 10:
            return item.quality + 2

        return item.quality + 1


class LegendaryQualityStrategy(QualityStrategy):
    def get_quality(self, item: Item):
        return item.quality


class LegendarySellStrategy(SellStrategy):
    def get_sell_date(self, item: Item):
        return item.sell_in


class ClassicSellStrategy(SellStrategy):
    def get_sell_date(self, item: Item):
        return item.sell_in - 1
