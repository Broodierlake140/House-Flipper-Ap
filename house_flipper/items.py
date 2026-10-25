from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from . import options as houseflipper_options

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
    "1$": 100001,
    "5$": 100005,
    "10$": 100010,
    "25$": 100025,
    "50$": 100050,
    "100$": 100100,
    "250$": 100250,
    "500$": 100500,
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
    "1$": ItemClassification.filler,
    "5$": ItemClassification.filler,
    "10$": ItemClassification.filler,
    "25$": ItemClassification.filler,
    "50$": ItemClassification.filler,
    "100$": ItemClassification.filler,
    "250$": ItemClassification.filler,
    "500$": ItemClassification.filler,
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
    money = world.options.starting_money.value
    add_money = 0
    
    money_list = []
    money_groups = {
        1: 0,
        5: 0,
        10: 0,
        25: 0,
        50: 0,
        100: 0,
        250: 0,
        500: 0,
        1000: 0,
        
    }
    for x in range(0, (money + 1)):
        if money >= 1000:
            money_groups[1000] + 1
            money - 1000
        elif money >= 500:
            money_groups[500] + 1
            money - 500
        elif money >= 250:
            money_groups[250] + 1
            money - 250
        elif money >= 100:
            money_groups[100] + 1
            money - 100
        elif money >= 50:
            money_groups[50] + 1
            money - 50
        elif money >= 25:
            money_groups[25] + 1
            money - 25
        elif money >= 10:
            money_groups[10] + 1
            money - 10
        elif money >= 5:
            money_groups[5] + 1
            money - 5
        elif money >= 1:
            money_groups[1] + 1
            money - 1
        else:
            break
            
    for x in money_groups:
        for i in range(0, money_groups[x]):
            world.push_precollected(world.create_item(str(x)+"$"))
    
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
