"""A simple text adventure game"""

#Initialize dictionaries, lists, etc., that are needed for our game to function.
player_inventory = {},
player_map = {},
current_room = '',
Rooms = [],
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
from objects import match
# Stage objects
living_room.stage_item([candle, match])
candle.look_object(player_inventory, current_room)
print("Attempt to pickup the candle.")
candle.pickup_object(player_inventory, current_room)
print("Here is the player's new inventory.")
print(player_inventory)
print("Here is the current room's inventory.")
living_room.room_inventory()
print("Now you drop the candle.")
candle.drop_object(player_inventory, current_room)
print("And here is the current room inventory:")
living_room.room_inventory()
candle.pickup_object(current_room, player_inventory)
print("Attempt to use candle alone.")
candle.use_object(current_room, player_inventory)

print("")
# You could store the candle object in a dict with the string 'candle' as the key? Then do dict[choice].look_object()
# candle.look_object(current_room)

# Start the main game loop.
while True:
    # Prompt player for a command and store as a string.
    choice = input('What do you want to do?\t')
    # Remove whitespace and split the choice string into a lowercase list.
    player_choice = choice.strip().lower().split()
    # Assign first list item to variable verb.
    verb = player_choice[0]
    # Delete 'up', 'at', 'with', 'on', to make player_choice list easier
    # to process.
    if 'up' in player_choice:
        player_choice.remove('up')
    if 'at' in player_choice:
        player_choice.remove('at')
    if 'with' in player_choice:
        player_choice.remove('with')
    if 'on' in player_choice:
        player_choice.remove('on')
    # Execute initial commands based on length of player_choice list and
    # exact verb chosen.
    if len(player_choice) == 1 and verb == 'look':
        noun = input(f'{verb.title()} at what?\t')
        if noun in current_room.room_inventory.keys():
            all_objects[noun].look_object()
    elif len(player_choice) == 1 and verb in ['use','take']:
        noun = input(f"What do you want to {verb}?\t")
        if verb == 'take':
            print('take')

    elif len(player_choice) == 2:
        verb = player_choice[0]
        noun = player_choice[1]

# print(player_choice)
# objects[choice].look_object(current_room)

