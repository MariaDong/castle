"""A simple text adventure game"""

#Initialize dictionaries, lists, etc., that are needed for our game to function.
player_inventory = {}
player_map = {}
current_room = ''
Rooms = []
Objects = []
"""The current_room variable tracks what room the player is in."""

# Import modules to model rooms and objects.
from class_models import Room
from class_models import Object
from time import sleep

# Import inital starting room
from rooms import living_room
# Set current room to starting room.
current_room = living_room
# Create objects to stage in room.
from objects import candle
# Stage objects
living_room.stage_item(candle)
candle.look_object(player_inventory, current_room)
print("Attempt to pickup the candle.")
candle.pickup_object(player_inventory, current_room)
print("Here is the player's new inventory.")
print(player_inventory)
print("Here is the current room's inventory.")
print(living_room.room_inventory())
print("Now you drop the candle.")
candle.drop_object(player_inventory, current_room)
print("And here is the current room inventory:")
print(current_room.room_inventory)

print("")
# You could store the candle object in a dict with the string 'candle' as the key? Then do dict[choice].look_object()
# candle.look_object(current_room)
# while True:
#     choice = input('What do you want to do?\t')
#     player_choice = choice.lower().split()
#     verb = player_choice[0]
#     if len(player_choice) == 1 and verb == 'look':
#         try: 
#             noun = input(f'{verb.title()} at what?\t')
#             if noun in objects.values():
#                 objects[noun].look_object(current_room)
#         except KeyError:
#             print(f"I'm not sure what a \"{noun}\" is.")
#     elif len(player_choice) == 1 and verb in ['use','take']:
#         noun = input(f"What do you want to {verb}?\t")
#         if verb == 'take':
#             objects[noun].pickup_object(player_inventory, current_room)
#     elif len(player_choice) == 2:
#         verb = player_choice[0]
#         noun = player_choice[1]

# print(player_choice)
# objects[choice].look_object(current_room)
