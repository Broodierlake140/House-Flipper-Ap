from __future__ import anotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from house_flipper.regions import HouseFlipperConnectionRules

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
    "Cleaning The Garage": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Cleaning The Garage"))
    ],
    "Radiators.": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Radiators."))
    ],
    "Amaranth Walls": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Amaranth Walls"))
    ],
    "Baby On The Way": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Baby on the way"))
    ],
    "Additional Walls": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Additional Walls"))
    ],
    "Walls To Knock Down": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Walls To Knock Down"))
    ],
    "Student's House To Clean Up": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Student's House To Clean Up"))
    ],
    "Save Me From These Horrible Colors Honey": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Save Me From These Horrible Colors Honey"))
    ],
    "Necessary Extra Bathroom": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Necessary Extra Bathroom"))
    ],
    "Bathroom And Home Workshop": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Bathroom And Home Workshop"))
    ],
    "Clean Up The House, Please": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Clean Up The House, Please"))
    ],
    "Aunt's Home To Redecorate": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Aunt's Home To Redecorate"))
    ],
    "House In Need Of A Renovation": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: House In Need Of A Renovation"))
    ],
    "Painting The House": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Painting The House"))
    ],
    "Garage :)": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Garage :)"))
    ],
    "Christmas Cleaning!": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Christmas Cleaning!"))
    ],
    "It's Christmas Once Again": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: It's Christmas Once Again"))
    ],
    "House To Refresh, Need Help!": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: House To Refresh, Need Help!"))
    ],
    "Kindergarten": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Kindergarten"))  
    ],
    "Sauna And Base Build": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Sauna And Base Build"))
    ],
    "All Out Gaming Room": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: All Out Gaming Room"))
    ],
    "Colorful Fiesta": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Colorful Fiesta"))
    ],
    "Let's Keep The Tradition Alive": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Let's Keep The Tradition Alive"))
    ],
    "What A Waste Of Money": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: What A Waste Of Money"))
    ],
    "Save My Christmas": [
        HouseFlipperConnectionRules("Menu", Has("Job Unlock: Save My Christmas"))
    ],
    
}

def create_and_connect_regions(world: HouseFlipperWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: HouseFlipperWorld) -> None:
    Regions = ["Ex-Boyfriend Stole The Radiator From My House", "Cleaning The Garage", "Radiators.", "Amaranth Walls", "Baby On The Way", "Additional Walls", "Walls To Knock Down", "Student's House To Clean Up", "Save Me From These Horrible Colors Honey", "Necessary Extra Bathroom", "Bathroom And Home Workshop", "Clean Up The House, Please", "Aunt's Home To Redecorate", "House In Need Of A Renovation", "Painting The House", "Garage :)", "Christmas Cleaning", "It's Christmas Once Again", "House To Refresh, Need Help!", "Kindergarten", "Sauna And Base Build", "All Out Gaming Room", "Colorful Fiesta", "Let's Keep The Tradition Alive", "What A Waste Of Money", "Save My Christmas"]
    for x in Regions:
        world.multiworld.regions += Region(x, world.player, world.multiworld)
    
def connect_regions(world: HouseFlipperWorld) -> None:
    for x in Regions_Connections:
         region = world.get_region(x)
             