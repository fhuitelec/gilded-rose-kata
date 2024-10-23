import copy
from abc import ABC, abstractmethod


def update_quality(items):
    return [item.update_quality() for item in items]


class QualityStrategy(ABC):
    @classmethod
    @abstractmethod
    def get_quality(self, item):
        pass


class SellStrategy(ABC):
    @abstractmethod
    def get_sell_date(self, item):
        pass


class Item:
    def __init__(
        self,
        name: str,
        quality_strategy: QualityStrategy,
        sell_strategy: SellStrategy,
        sell_in: int,
        quality: int
    ):
        self.name = name
        self.quality_strategy = quality_strategy
        self.sell_strategy = sell_strategy
        self.sell_in = sell_in
        self.quality = quality

    def update_quality(self) -> "Item":
        sell_in = self.sell_strategy.get_sell_date(self)
        quality = self.quality_strategy.get_quality(self)

        quality = max(quality, 0)
        quality = min(quality, 50)

        return Item(self.name, self.quality_strategy, self.sell_strategy, sell_in, quality)

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
