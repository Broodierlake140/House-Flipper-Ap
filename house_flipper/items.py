from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import HouseFlipperWorld
    
ITEM_NAME_TO_ID = {
    "Mop": 1,
    "Window Cleaner": 2,
    "Painting Tool": 3,
    "Demolition Tool": 4,
    "Build Walls Tool": 5,
    
    #Job Unlocks, Start at 1k
    "Job Unlock: Cleaning The Garage": 1002,
    "Job Unlock: Radiators.": 1003,
    "Job Unlock: Amaranth Walls": 1004,
    "Job Unlock: Baby On The Way": 1005,
    "Job Unlock: Additional Walls": 1006,
    "Job Unlock: Walls To Knock Down": 1007,
    
    #Money Start at 100k
    "250$": 100250,
    "500$": 100500,
    "750$": 100750,
    "1000$": 101000,
    
    
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Mop": ItemClassification.progression,
    "Window Cleaner": ItemClassification.progression,
    "Painting Tool": ItemClassification.progression,
    "Demolition Tool": ItemClassification.progression,
    "Build Walls Tool": ItemClassification.progression,

    #Job Unlocks
    "Job Unlock: Cleaning The Garage": ItemClassification.progression,
    "Job Unlock: Radiators.": ItemClassification.progression,
    "Job Unlock: Amaranth Walls": ItemClassification.progression,
    "Job Unlock: Baby On The Way": ItemClassification.progression,
    "Job Unlock: Additional Walls": ItemClassification.progression,
    "Job Unlock: Walls To Knock Down": ItemClassification.progression,

    #Money
    "250$": ItemClassification.filler,
    "500$": ItemClassification.filler,
    "750$": ItemClassification.filler,
    "1000$": ItemClassification.filler,
}

class HouseFlipperItem(Item):
    game = "House Flipper"


def get_random_filler_item_name(world: HouseFlipperWorld) -> str:
    int = world.random.randint(0, 100)
    if int < 61:
        return "250$"
    elif int > 60 & int < 81:
        return "500$"
    elif int > 80 & int < 90:
        return "750$"
    else:
        return "1000$"


def create_item_with_correct_classification(world: HouseFlipperWorld, name:str) -> HouseFlipperItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return HouseFlipperItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: HouseFlipperWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Mop"),
        world.create_item("Window Cleaner"),
        world.create_item("Painting Tool"),
        world.create_item("Demolition Tool"),
        world.create_item("Build Walls Tool"),
        world.create_item("Job Unlock: Cleaning The Garage"),
        world.create_item("Job Unlock: Radiators."),
        world.create_item("Job Unlock: Amaranth Walls"),
        world.create_item("Job Unlock: Baby On The Way"),
        world.create_item("Job Unlock: Additional Walls"),
        world.create_item("Job Unlock: Walls To Knock Down"),
    ]
    num = len(itempool)

    num_locations = len(world.multiworld.get_unfilled_locations(world.player))
    filler_needed = num_locations - num
    itempool += [world.create_filler() for _ in range(filler_needed)]

    world.multiworld.itempool += itempool
