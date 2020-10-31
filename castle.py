"""A simple text adventure game"""

#-----------1.0 INITIALIZE OBJECTS, ROOMS, AND MESSAGES.----------------

# Import modules to model rooms and objects.
from time import sleep

#Initialize the player.
from class_models import Player
player = Player()

#Initialize the Rooms, Objects, and functions.
from rooms import *
from objects import *
from functions import *

#Stage rooms with objects.
from staging import rooms_to_stage, items_to_stage, paired_items
stage_rooms(rooms_to_stage, items_to_stage)
pair_items(paired_items)

# Initialize stock messages used in while loop - these are constant and do not
# change through the game.
try_again = "\n\tI don't think I understood that. Maybe tell me a different way?"
inventory_message = "\n\tHere are the things in your inventory. Use LOOK to "
inventory_message +="examine any of them closer."
help_message = """\n\tHere is a list of commands you can use: MAP, INVENTORY, 
LOOK, TAKE, USE."""


# # Greet the player.
# print("Hi, Player!")
# # # Get the player's name.
# player.get_name()
# # Orient the reader to available commands:
# print("Intro text or something.")

player.enter_room(parlor)

# The get_command function asks the player what they want to do and sanitizes
# the input so that it can be processed by the main game loop.

# Start the main game loop.
while True:
    choice = get_command()
    if choice[0] == 'inventory':
        player_inventory(player, inventory_message)
# If the player chooses 'help', a list of commands is printed.
    elif choice[0] == 'help':
        print(help_message)
# If the verb is 'look' or 'examine':
    elif choice[0] == 'look' or choice[0] == 'examine':
# Check to see if the next work is 'room' or the current room.
        if choice[1] == 'room' or choice[1] == player.current_room.slug:
# If so, run the look_room method from player.
            player.look_room()
# Otherwise, run the look_object method from player.
        else:
            player_look_object(choice, player)
# If the player chooses take or a similar word, run take_object method.
    elif choice[0] == 'take' or choice[0] == 'pick' or choice[0] == 'pickup':
        player_take_object(choice, player)
# The drop command works the same, executing the drop_object method.

    elif choice[0] == 'drop':
        player_drop_object(choice, player)

# The 'use' command triggers different commands depending on how many
# nouns the player has chosen.

    elif choice[0] == 'use':
        # If player has only entered one noun, run player_use_one().
        if len(choice) == 2:
            player_use_one(choice, player)
        # if player has entered 2 nouns, run player_use_two().
        elif len(choice) == 3:
            player_use_two(choice, player)
        else:
            print("\n\tThese are too many objects to use together.")
    
# establish a pass at end of loop in case no conditions are met.
    else: 
        print(try_again)
