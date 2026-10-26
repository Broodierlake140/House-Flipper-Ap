from __future__ import annotations

import logging
from logging import log
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from rule_builder.rules import Has, HasAll, Rule, True_


if TYPE_CHECKING:
    from .world import HouseFlipperWorld
    
from dataclasses import dataclass 

@dataclass
class HouseFlipperConnectionRules():
    source: str
    rule: Rule
   
   
   
regions_rules_tables: dict[str, list[HouseFlipperConnectionRules]] = {
    "Ex-Boyfriend Stole The Radiator From My House": [
        HouseFlipperConnectionRules("Menu", True_())
    ],
    "Ex-Boyfriend Stole The Radiator From My House - Mop": [
        HouseFlipperConnectionRules("Ex-Boyfriend Stole The Radiator From My House", Has("Mop"))
    ],
    "Cleaning The Garage": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Cleaning The Garage"))
    ],
    "Cleaning The Garage - Mop": [
        HouseFlipperConnectionRules("Cleaning The Garage", Has("Mop"))
    ],
    "Cleaning The Garage - Window Cleaner": [
        HouseFlipperConnectionRules("Cleaning The Garage", Has("Window Cleaner"))
    ],
    "Cleaning The Garage - Completions": [
        HouseFlipperConnectionRules("Cleaning The Garage", HasAll("Window Cleaner", "Mop"))
    ],
    "Radiators.": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Radiators."))
    ],
    "Amaranth Walls": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Amaranth Walls"))
    ],
    "Amaranth Walls - Living Room: Painting": [
        HouseFlipperConnectionRules("Amaranth Walls", Has("Painting Tool"))
    ],
    "Baby On The Way": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Baby On The Way"))
    ],
    "Baby On The Way - Mop": [
        HouseFlipperConnectionRules("Baby On The Way", Has("Mop"))
    ],
    "Baby On The Way - Painting": [
        HouseFlipperConnectionRules("Baby On The Way", Has("Painting Tool"))
    ],
    "Baby On The Way - Window Cleaner": [
        HouseFlipperConnectionRules("Baby On The Way", Has("Window Cleaner"))
    ],
    "Baby On The Way - Completions": [
        HouseFlipperConnectionRules("Baby On The Way", HasAll("Mop", "Window Cleaner", "Painting Tool"))
    ],
    "Baby On The Way - Living Room": [
        HouseFlipperConnectionRules("Baby On The Way", HasAll("Mop", "Window Cleaner"))
    ],
    "Additional Walls": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Additional Walls"))
    ],
    "Additional Walls - Demolition": [
        HouseFlipperConnectionRules("Additional Walls", Has("Demolition Tool"))
    ],
    "Additional Walls - Build Walls": [
        HouseFlipperConnectionRules("Additional Walls", Has("Build Walls Tool"))
    ],
    "Additional Walls - Completions": [
        HouseFlipperConnectionRules("Additional Walls", HasAll("Build Walls Tool", "Demolition Tool"))
    ],
    "Walls To Knock Down": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Walls To Knock Down"))
    ],
    "Walls To Knock Down - Demolition": [
        HouseFlipperConnectionRules("Walls To Knock Down", Has("Demolition Tool"))
    ],
    "Walls To Knock Down - Paint": [
        HouseFlipperConnectionRules("Walls To Knock Down", Has("Painting Tool"))
    ],
    "Walls To Knock Down - Completions": [
        HouseFlipperConnectionRules("Walls To Knock Down", HasAll("Demolition Tool", "Painting Tool"))
    ],
}

def create_and_connect_regions(world: HouseFlipperWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: HouseFlipperWorld) -> None:
    region_list = [Region("Menu", world.player, world.multiworld)]
    for x in regions_rules_tables.keys():
        region_list.append(Region(x, world.player, world.multiworld))
    world.multiworld.regions += region_list

def connect_regions(world: HouseFlipperWorld) -> None:
    for x in regions_rules_tables.keys():
        for entrance in regions_rules_tables[x]:
            world.create_entrance(world.get_region(entrance.source), world.get_region(x), entrance.rule)
