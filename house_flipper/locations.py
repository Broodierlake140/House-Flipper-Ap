from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from rule_builder.rules import HasAll, HasFromList, Has, OptionFilter
from . import options as houseflipper_options
from . import items

from dataclasses import dataclass

if TYPE_CHECKING:
    from .world import HouseFlipperWorld

class HouseFlipperLocation(Location):
    game = "House Flipper"

@dataclass()
class event_info():
    location: str
    item: str


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

LOCATION_NAME_TO_ID = {
    #Ex-Boyfriend Stole The Radiator From My House
    "Ex-Boyfriend Stole The Radiator From My House: Complete": 1000,
    
    #Ex-Boyfriend Stole The Radiator From My House: Living Room
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Complete": 1010,
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Remove Trash": 1011,
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Clean Dirt": 1012,
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Mount Radiator": 1013,
    
    #Ex-Boyfriend Stole The Radiator From My House: Bedroom
    "Ex-Boyfriend Stole The Radiator From My House - Bedroom: Complete": 1020,
    "Ex-Boyfriend Stole The Radiator From My House - Bedroom: Remove trash": 1021,
    "Ex-Boyfriend Stole The Radiator From My House - Bedroom: Clean Dirt": 1022,
    
    #Ex-Boyfriend Stole The Radiator From My House: Bathroom
    "Ex-Boyfriend Stole The Radiator From My House - Bathroom: Complete": 1030,
    "Ex-Boyfriend Stole The Radiator From My House - Bathroom: Clean Dirt": 1031,

    #Cleaning The Garage
    "Cleaning The Garage: Complete": 2000,
    "Cleaning The Garage: Remove Trash ": 2001,
    "Cleaning The Garage: Clean Dirt": 2002,
    "Cleaning The Garage: Clean The Window": 2003,

    #Radiators
    "Radiators.: Complete": 3000,

    #Radiators: Bedroom
    "Radiators. - Bedroom: Complete": 3010,
    "Radiators. - Bedroom: Mount Radiator": 3011,

    #Radiators: Office
    "Radiators. - Office: Complete": 3020,
    "Radiators. - Office: Mount Radiator": 3021,

    #Radiators: Toilet
    "Radiators. - Toilet: Complete": 3030,
    "Radiators. - Toilet: Mount Sink": 3031,
    "Radiators. - Toilet: Mount Towel Radiator": 3032,

    #Amaranth Walls
    "Amaranth Walls: Complete": 4000,

    #Amaranth Walls: Corridor
    "Amaranth Walls - Corridor: Complete": 4010,
    "Amaranth Walls - Corridor: Repair Electrical Outlet": 4011,

    #Amaranth Walls: Living Room
    "Amaranth Walls - Living Room With Kitchenette: Complete": 4020,
    "Amaranth Walls - Living Room With Kitchenette: Repair Electrical Outlet": 4021,
    "Amaranth Walls - Living Room With Kitchenette: Paint": 4022,

    #Baby On The Way
    "Baby On The Way: Complete": 5000,

    #Baby On The Way: Room
    "Baby On The Way - Room: Complete": 5010,
    "Baby On The Way - Room: Remove Trash": 5011,
    "Baby On The Way - Room: Clean Dirt": 5012,
    "Baby On The Way - Room: Clean The Windows": 5013,
    "Baby On The Way - Room: Paint": 5014,
    "Baby On The Way - Room: Place Crib": 5015,
    "Baby On The Way - Room: Place Bookcase": 5016,
    "Baby On The Way - Room: Place Cabinet With Changing Table": 5017,
    "Baby On The Way - Room: Place Both Poufs": 5018,

    #Baby On The Way: Corridor
    "Baby On The Way - Corridor: Complete": 5020,
    "Baby On The Way - Corridor: Remove Trash": 5021,
    "Baby On The Way - Corridor: Clean Dirt": 5022,

    #Baby On The Way: Living Room
    "Baby On The Way - Living Room: Complete": 5030,
    "Baby On The Way - Living Room: Remove Trash": 5031,
    "Baby On The Way - Living Room: Remove Dirt": 5032,
    "Baby On The Way - Living Room: Clean The Windows": 5033,

    #Baby On The Way: Bedroom
    "Baby On The Way - Bedroom: Complete": 5040,
    "Baby On The Way - Bedroom: Remove Trash": 5041,
    "Baby On The Way - Bedroom: Clean Dirt": 5042,
    "Baby On The Way - Bedroom: Clean Windows": 5043,

    #Baby On The Way: Bathroom
    "Baby On The Way - Bathroom: Complete": 5050,
    "Baby On The Way - Bathroom: Clean Dirt": 5051,
    "Baby On The Way - Bathroom: Clean Windows": 5052,
    
    
    #Additional Walls
    "Additional Walls: Complete": 6000,
    
    #Additional Walls: Children's Room
    "Additional Walls - Children's Room: Complete": 6010,
    "Additional Walls - Children's Room: Repair Electrical Outlet": 6011,
    "Additional Walls - Children's Room: Destroy Walls": 6012,
    "Additional Walls - Children's Room: Build Walls": 6013,
    "Additional Walls - Children's Room: Remove Crib": 6014,
    "Additional Walls - Children's Room: Place Bed Grill": 6015,
    
    #Additional Walls: Room
    "Additional Walls - Room: Complete": 6020,
    "Additional Walls - Room: Destroy Walls": 6021,

    #Additional Walls: Living Room
    "Additional Walls - Living Room: Complete": 6030,
    "Additional Walls - Living Room: Repair Electrical Outlet": 6031,


    #Walls To Knock Down
    "Walls To Knock Down: Complete": 7000,
    
    #Walls To Knock Down: Living Room
    "Walls To Knock Down - Living Room: Complete": 7010,
    "Walls To Knock Down - Living Room: Destroy The Walls": 7011,

    #Walls To Knock Down: Corridor
    "Walls To Knock Down - Corridor: Complete": 7020,
    "Walls To Knock Down - Corridor: Destroy The Walls": 7021,

    #Walls To Knock Down: Large Kitchen
    "Walls To Knock Down - Large Kitchen: Complete": 7030,
    "Walls To Knock Down - Large Kitchen: Destroy Walls": 7031,

    #Walls To Knock Down: Bedroom
    "Walls To Knock Down - Bedroom: Complete": 7040,
    "Walls To Knock Down - Bedroom: Paint Walls": 7041,
    
}

Location_Regions = {
    #Ex-Boyfriend Stole The Radiator From My House
    "Ex-Boyfriend Stole The Radiator From My House: Complete": "Ex-Boyfriend Stole The Radiator From My House - Mop",

    #Ex-Boyfriend Stole The Radiator From My House: Living Room
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Complete": "Ex-Boyfriend Stole The Radiator From My House - Mop",
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Remove Trash": "Ex-Boyfriend Stole The Radiator From My House",
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Clean Dirt": "Ex-Boyfriend Stole The Radiator From My House - Mop",
    "Ex-Boyfriend Stole The Radiator From My House - Living Room: Mount Radiator": "Ex-Boyfriend Stole The Radiator From My House",
    
    #Ex-Boyfriend Stole The Radiator From My House: Bedroom
    "Ex-Boyfriend Stole The Radiator From My House - Bedroom: Complete": "Ex-Boyfriend Stole The Radiator From My House - Mop",
    "Ex-Boyfriend Stole The Radiator From My House - Bedroom: Remove trash": "Ex-Boyfriend Stole The Radiator From My House",
    "Ex-Boyfriend Stole The Radiator From My House - Bedroom: Clean Dirt": "Ex-Boyfriend Stole The Radiator From My House - Mop",
    
    #Ex-Boyfriend Stole The Radiator From My House: Bathroom
    "Ex-Boyfriend Stole The Radiator From My House - Bathroom: Complete": "Ex-Boyfriend Stole The Radiator From My House - Mop",
    "Ex-Boyfriend Stole The Radiator From My House - Bathroom: Clean Dirt": "Ex-Boyfriend Stole The Radiator From My House - Mop",
    
    #Cleaning The Garage
    "Cleaning The Garage: Complete": "Cleaning The Garage - Completions",
    "Cleaning The Garage: Remove Trash ": "Cleaning The Garage",
    "Cleaning The Garage: Clean Dirt": "Cleaning The Garage - Mop",
    "Cleaning The Garage: Clean The Window": "Cleaning The Garage - Window Cleaner",
    
    #Radiators
    "Radiators.: Complete": "Radiators.",
    
    #Radiators: Bedroom
    "Radiators. - Bedroom: Complete": "Radiators.",
    "Radiators. - Bedroom: Mount Radiator": "Radiators.",
    
    #Radiators: Office
    "Radiators. - Office: Complete": "Radiators.",
    "Radiators. - Office: Mount Radiator": "Radiators.",
    
    #Radiators: Toilet
    "Radiators. - Toilet: Complete": "Radiators.",
    "Radiators. - Toilet: Mount Sink": "Radiators.",
    "Radiators. - Toilet: Mount Towel Radiator": "Radiators.",
    
    #Amaranth Walls
    "Amaranth Walls: Complete": "Amaranth Walls - Living Room: Painting",
    
    #Amaranth Walls: Corridor
    "Amaranth Walls - Corridor: Complete": "Amaranth Walls",
    "Amaranth Walls - Corridor: Repair Electrical Outlet": "Amaranth Walls",
    
    #Amaranth Walls: Living Room
    "Amaranth Walls - Living Room With Kitchenette: Complete": "Amaranth Walls - Living Room: Painting",
    "Amaranth Walls - Living Room With Kitchenette: Repair Electrical Outlet": "Amaranth Walls",
    "Amaranth Walls - Living Room With Kitchenette: Paint": "Amaranth Walls - Living Room: Painting",
    
    #Baby On The Way
    "Baby On The Way: Complete": "Baby On The Way - Completions",
    
    #Baby On The Way: Room
    "Baby On The Way - Room: Complete": "Baby On The Way - Completions",
    "Baby On The Way - Room: Remove Trash": "Baby On The Way",
    "Baby On The Way - Room: Clean Dirt": "Baby On The Way - Mop",
    "Baby On The Way - Room: Clean The Windows": "Baby On The Way - Window Cleaner",
    "Baby On The Way - Room: Paint":  "Baby On The Way - Painting",
    "Baby On The Way - Room: Place Crib": "Baby On The Way",
    "Baby On The Way - Room: Place Bookcase": "Baby On The Way",
    "Baby On The Way - Room: Place Cabinet With Changing Table": "Baby On The Way",
    "Baby On The Way - Room: Place Both Poufs": "Baby On The Way",
    
    #Baby On The Way: Corridor
    "Baby On The Way - Corridor: Complete": "Baby On The Way - Mop",
    "Baby On The Way - Corridor: Remove Trash": "Baby On The Way",
    "Baby On The Way - Corridor: Clean Dirt": "Baby On The Way - Mop",
    
    #Baby On The Way: Living Room
    "Baby On The Way - Living Room: Complete": "Baby On The Way - Living Room",
    "Baby On The Way - Living Room: Remove Trash": "Baby On The Way",
    "Baby On The Way - Living Room: Remove Dirt": "Baby On The Way - Mop",
    "Baby On The Way - Living Room: Clean The Windows": "Baby On The Way - Window Cleaner",
    
    #Baby On The Way: Bedroom
    "Baby On The Way - Bedroom: Complete": "Baby On The Way - Living Room",
    "Baby On The Way - Bedroom: Remove Trash": "Baby On The Way",
    "Baby On The Way - Bedroom: Clean Dirt": "Baby On The Way - Mop",
    "Baby On The Way - Bedroom: Clean Windows": "Baby On The Way - Window Cleaner",
    
    #Baby On The Way: Bathroom
    "Baby On The Way - Bathroom: Complete": "Baby On The Way - Living Room",
    "Baby On The Way - Bathroom: Clean Dirt": "Baby On The Way - Mop",
    "Baby On The Way - Bathroom: Clean Windows": "Baby On The Way - Window Cleaner",
    
    
    #Additional Walls
    "Additional Walls: Complete": "Additional Walls - Completions",
    
    #Additional Walls: Children's Room
    "Additional Walls - Children's Room: Complete": "Additional Walls - Completions",
    "Additional Walls - Children's Room: Repair Electrical Outlet": "Additional Walls",
    "Additional Walls - Children's Room: Destroy Walls": "Additional Walls - Demolition",
    "Additional Walls - Children's Room: Build Walls": "Additional Walls - Build Walls",
    "Additional Walls - Children's Room: Remove Crib": "Additional Walls",
    "Additional Walls - Children's Room: Place Bed Grill": "Additional Walls",
    
    #Additional Walls: Room
    "Additional Walls - Room: Complete": "Additional Walls - Demolition",
    "Additional Walls - Room: Destroy Walls": "Additional Walls - Demolition",
    
    #Additional Walls: Living Room
    "Additional Walls - Living Room: Complete": "Additional Walls",
    "Additional Walls - Living Room: Repair Electrical Outlet": "Additional Walls",
    
    
    #Walls To Knock Down
    "Walls To Knock Down: Complete": "Walls To Knock Down - Completions",
    
    #Walls To Knock Down: Living Room
    "Walls To Knock Down - Living Room: Complete": "Walls To Knock Down - Demolition",
    "Walls To Knock Down - Living Room: Destroy The Walls": "Walls To Knock Down - Demolition",
    
    #Walls To Knock Down: Corridor
    "Walls To Knock Down - Corridor: Complete": "Walls To Knock Down - Demolition",
    "Walls To Knock Down - Corridor: Destroy The Walls": "Walls To Knock Down - Demolition",
    
    #Walls To Knock Down: Large Kitchen
    "Walls To Knock Down - Large Kitchen: Complete": "Walls To Knock Down - Demolition",
    "Walls To Knock Down - Large Kitchen: Destroy Walls": "Walls To Knock Down - Demolition",
    
    #Walls To Knock Down: Bedroom
    "Walls To Knock Down - Bedroom: Complete": "Walls To Knock Down - Paint",
    "Walls To Knock Down - Bedroom: Paint Walls": "Walls To Knock Down - Paint",

}
event_locations: dict[str, list[event_info]] = {
    "Ex-Boyfriend Stole The Radiator From My House - Mop": [
        event_info("Completed Ex-Boyfriend Stole The Radiator From My House", "Completed Ex-Boyfriend Stole The Radiator From My House")
    ],
    "Cleaning The Garage - Completions": [
        event_info("Completed Cleaning The Garage", "Completed Cleaning The Garage")
    ],
    "Radiators.": [
        event_info("Completed Radiators.", "Completed Radiators.")
    ],
    "Amaranth Walls - Living Room: Painting": [
        event_info("Completed Amaranth Walls", "Completed Amaranth Walls")
    ],
    "Baby On The Way - Completions": [
        event_info("Completed Baby On The Way", "Completed Baby On The Way")
    ],
    "Additional Walls - Completions" : [
        event_info("Completed Additional Walls", "Completed Additional Walls")
    ],
    "Walls To Knock Down - Completions" : [
        event_info("Completed Walls To Knock Down", "Completed Walls To Knock Down")
    ],
}
    



def create_all_locations(world: HouseFlipperWorld) -> None:
    create_events(world)
    create_regular_locations(world)


def create_regular_locations(world: HouseFlipperWorld) -> None:
    for x in Location_Regions.keys():
        region = world.get_region(Location_Regions[x])
        loc = get_location_names_with_ids([x])
        region.add_locations(loc, HouseFlipperLocation)
        

def  goal(string: str):
    goal_list = []
    if houseflipper_options.Ex == True:
        goal_list.append("Completed Ex-Boyfriend Stole The Radiator From My House")
    if houseflipper_options.Garage == True:
        goal_list.append("Completed Cleaning The Garage")
    if houseflipper_options.Radiators == True:
        goal_list.append("Completed Radiators.")
    if houseflipper_options.Amaranth == True:
        goal_list.append("Completed Amaranth Walls")
    if houseflipper_options.Baby == True:
        goal_list.append("Completed Baby On The Way")
    if houseflipper_options.AddWalls == True:
        goal_list.append("Completed Additional Walls")
    if houseflipper_options.KnockWalls == True:
        goal_list.append("Completed Walls To Knock Down")
    if not goal_list:
        goal_list.append("Completed Ex-Boyfriend Stole The Radiator From My House")
    for str in goal_list:
        logging.info(goal_list)
        logging.info("String")
        if str == string:
            logging.info(str)
            return str
    return ""
def create_events(world: HouseFlipperWorld) -> None:
    for x in event_locations.keys():
            for loc in event_locations[x]:
                if goal(loc.location) != "":
                    #logging.info(loc.location)
                    region = world.get_region(x)
                    region.add_event(loc.location, loc.item)
                    
    world.set_completion_rule(
        ((Has("Completed Ex-Boyfriend Stole The Radiator From My House") | OptionFilter(houseflipper_options.Ex, 1))
         | [OptionFilter(houseflipper_options.Ex, 0),
         OptionFilter(houseflipper_options.Garage, 0),
         OptionFilter(houseflipper_options.Radiators, 0),
         OptionFilter(houseflipper_options.Amaranth, 0), 
         OptionFilter(houseflipper_options.Baby, 0), 
         OptionFilter(houseflipper_options.AddWalls, 0),
         OptionFilter(houseflipper_options.KnockWalls, 0)]) &
        (Has("Completed Cleaning The Garage") | OptionFilter(houseflipper_options.Garage, 0)) &
        (Has("Completed Radiators.") | OptionFilter(houseflipper_options.Radiators, 0)) &
        (Has("Completed Amaranth Walls") | OptionFilter(houseflipper_options.Amaranth, 0)) &
        (Has("Completed Baby On The Way") | OptionFilter(houseflipper_options.Baby, 0)) &
        (Has("Completed Additional Walls") | OptionFilter(houseflipper_options.AddWalls, 0)) &
        (Has("Completed Walls To Knock Down") | OptionFilter(houseflipper_options.KnockWalls, 0)) 
    )
