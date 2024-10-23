from gilded_rose.gilded_rose import Item
from dataclasses import dataclass
from typing import Self


SULFURAS = "Sulfuras, Hand of Ragnaros"
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"


@dataclass
class ItemBuilder:
    name: str = None
    ennobles: bool = False
    legendary: bool = False
    backstage: bool = False
    sell_date: int = 4
    quality: int = 5

    def with_name(self, name: str) -> Self:
        self.name = name
        return self

    def with_quality(self, quality: int) -> Self:
        self.quality = quality
        return self

    def with_sell_date(self, sell_date: int) -> Self:
        self.sell_date = sell_date
        return self

    def that_ennobles_with_time(self) -> Self:
        if self.legendary:
            raise ItemCannotBeLegendaryAndEnnobleWithTime()
        self.ennobles = True
        return self

    def that_is_legendary(self) -> Self:
        if self.ennobles:
            raise ItemCannotBeLegendaryAndEnnobleWithTime()
        self.legendary = True
        return self

    def that_is_backstage(self) -> Self:
        self.backstage = True
        return self

    def build(self) -> Item:
        return Item(
            self._name(),
            ennobles=self.ennobles,
            legendary=self.legendary,
            backstage=self.backstage,
            sell_in=self.sell_date,
            quality=self.quality
        )

    def _name(self) -> str:
        if self.name is not None:
            return self.name
        if self.ennobles:
            return AGED_BRIE
        if self.legendary:
            return SULFURAS
        return "foo"


def given_an_item():
    return ItemBuilder()


def ItemCannotBeLegendaryAndEnnobleWithTime(ValueError):
    def __init__(self):
        super().__init__("An item cannot ennoble with time and be legendary at the same time")
