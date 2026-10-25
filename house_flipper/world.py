from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World

from . import items, locations, regions, web_world
from rule_builder.rules import HasAll
from . import options as houseflipper_options


class HouseFlipperWorld(World):
    game = "House Flipper"
    
    web = web_world.HouseFlipperWebWorld()
    
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    options_dataclass = houseflipper_options.HouseFlipperOptions
    options = houseflipper_options.HouseFlipperOptions


    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)
    
    def create_items(self) -> None:
        items.create_all_items(self)
        
        
    
    def create_item(self, name: str) -> items.HouseFlipperItem:
        return items.create_item_with_correct_classification(self, name)
    

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    
        