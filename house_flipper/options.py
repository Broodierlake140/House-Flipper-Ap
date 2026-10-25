from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice, OptionGroup, OptionSet, OptionList, Option, Range, DefaultOnToggle

class Ex(DefaultOnToggle):
    display_name = "Ex-Boyfriend Stole The Radiator From My House"
class Garage(DefaultOnToggle):
    display_name = "Cleaning The Garage"
class Radiators(DefaultOnToggle):
    display_name = "Radiators."
class Amaranth(DefaultOnToggle):
    display_name = "Amaranth Walls"
class Baby(DefaultOnToggle):
    display_name = "Baby On The Way"
class AddWalls(DefaultOnToggle):
    display_name = "Additional Walls"
class KnockWalls(DefaultOnToggle):
    display_name = "Walls To Knock Down"
class StartingMoney(Range):
    range_start = 0
    range_end = 99999
    default = 0
    display_name = "Starting Money"
@dataclass
class HouseFlipperOptions(PerGameCommonOptions):
    starting_money: StartingMoney
    ex: Ex
    garage: Garage
    radiators: Radiators
    amaranth: Amaranth
    baby: Baby
    add_walls: AddWalls
    knock_walls: KnockWalls


option_groups = [
    OptionGroup(
        "Goal Levels",
        [Ex, Garage, Radiators, Amaranth, Baby, AddWalls, KnockWalls],
    ),
]