from gilded_rose.gilded_rose import Item, GildedRose
from dataclasses import dataclass
from typing import Self
from tests.test_gilded_rose_brie import AGED_BRIE

@dataclass
class ItemBuilder:
    ennobles: bool = False
    quality: int = 5

    def with_quality(self, quality: int) -> Self:
        self.quality = quality
        return self

    def that_ennobles_with_time(self) -> Self:
        self.ennobles = True
        return self

    def build(self) -> Item:
        name = AGED_BRIE if self.ennobles else "foo"
        return Item(name, sell_in=2, quality=self.quality)


def given_an_item():
    return ItemBuilder()
