from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import HouseFlipperWorld

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
    "Baby On The Way - Living Room: Clean The Windows": 5032,

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
    
    
    #Student's House To Clean Up
    "Student's House To Clean Up": 8000,
    
    #Student's House To Clean Up: 
}
