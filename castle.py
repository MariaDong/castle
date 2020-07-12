"""A simple text adventure game"""

#Initialize dictionaries, lists, etc., that are needed for our game to function.
player_inventory = {}
player_map = {}
current_room = ''
"""The current_room variable tracks the player's location."""
Rooms = {}
all_objects = {}
"""This is a global dictionary that stores a copy of all objects and rooms in 
the game as they're introduced. Class methods for Object class and Room class
also update this dictionary as objects change, e.g., if a candle is used. This
simplifies the while loop used to interface with the game; although objects are
compared with the class-based dictionaries for the current room, descriptions
are retrieved from the global dictionary and require no conversion."""

# Import modules to model rooms and objects.
from time import sleep
from class_models import Object
from class_models import Room
"""Used to introduce a delay as needed to make information parsing easier."""

# Import the rooms used in the game.
from rooms import parlor
# Import the objects used in the game.
from objects import candle, match
from objects import test_object
test_object.add_dict(all_objects)
# Add objects to lists to be staged.
parlor_staging = [candle, match]
# Call stage item method to move objects to room inventories and all_objects.
parlor.stage_item(all_objects, staged=parlor_staging)
current_room = parlor

# Initialize stock messages used in while loop - these are constant and do not
# change through the game.
try_again = "I don't think I understood that. Maybe tell me a different way?"
inventory_message = "Here are the things in your inventory. Use LOOK to "
inventory_message +="examine any of them closer."
help_message = """Here is a list of commands you can use: MAP, INVENTORY, LOOK,
TAKE, USE."""

# Start the main game loop.
while True:
    # Prompt player for a command and store as a string.
    choice = input('What do you want to do?\t\t')
    # Sanitize input:
    # Remove whitespace and split the choice string into a lowercase list.
    player_choice = choice.strip().lower().split()
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
    # Assign first item in player_choice to the 'verb' variable, then execute commands.
    verb = player_choice[0]
    # COMMAND TREE:
    # If verb == 'inventory', a pre-set inventory intro message,
    # 'inventory_message', is printed. An empty dictionary is created, and
    # then a for loop appends the dictionary with all of the keys from the
    # player_inventory dictionary in title case. The list is then 
    # printed, producing a neatly formatted inventory.
    if verb == 'inventory':
        print(inventory_message)
        formatted_inventory_list = []
        for item in player_inventory.keys():
            formatted_inventory_list.append(item.title())
        print(formatted_inventory_list)
    # If the player chooses 'help', a list of commands is printed.
    elif verb == 'help':
        print(help_message)
    # If the player chooses 'look', the player is either prompted to provide
    # the Object they are looking at, or the Object is parsed via its position
    # in the player_choice list. The object is assigned to 'noun'. If noun = 
    # 'room', the look_room method is called for the current_room. Otherwise,
    # 'noun' is used as the key for the global_objects dict to call the 
    # look_object method for the Object instance. 
    # # If the player_choice list has too many items (e.g., player typed "look
    # bell window", the "try_again" string is printed.)
    elif verb == 'look' or verb == 'examine':
        if len(player_choice) > 2:
            print(try_again)
        elif len(player_choice) == 2:
            noun = player_choice[1]
            if noun == 'room':
                current_room.look_room(current_room)
            else:
                try:
                    all_objects[noun].look_object(player_inventory, current_room)
                except:
                    print(f"I don't know what \"{noun}\" means.")
        elif len(player_choice) == 1:
            noun = input('Look at what?\t')
            if noun == 'room':
                current_room.look_room(current_room)
            else:
                try:
                    all_objects[noun].look_object(player_inventory, current_room)
                except:
                    print(f"I don't know what \"{noun}\" means.")
        else:
            pass
    # The take command behaves in a similar fashion and executes the
    # pickup_object method from Object instance.
    elif verb == 'take' or verb == 'pick' or verb == 'pickup':
        if len(player_choice) > 2:
            print(try_again)
        elif len(player_choice) == 1:
            noun = input('Take what?\t')
            try: 
                all_objects[noun].pickup_object(player_inventory, current_room)
            except:
                print(f"I don't know what \"{noun}\" means.")
        elif len(player_choice) == 2:
            noun = player_choice[1]
            try: 
                all_objects[noun].pickup_object(player_inventory, current_room)
            except:
                print(f"I don't know what \"{noun}\" means.")
    # The drop commands executes drop_object method from Object instance.
    elif verb == 'drop':
        if len(player_choice) > 2:
            print(try_again)
        elif len(player_choice) == 1:
            noun = input('Drop what?\t')
            try: 
                all_objects[noun].drop_object(player_inventory, current_room)
            except:
                print(f"I don't know what \"{noun}\" means.")
        elif len(player_choice) == 2:
            noun = player_choice[1]
            try: 
                all_objects[noun].drop_object(player_inventory, current_room)
            except:
                print(f"I don't know what \"{noun}\" means.")

    # The following commands are for troubleshooting only.
    elif verb == 'inventory_long':
        print(player_inventory)
    elif verb == 'room_inventory':
        current_room.print_inventory()
    elif verb == 'room_inventory_long':
        current_room.print_inventory_long()
    # Finally, an 'else' to capture any misunderstood commands.
    else:
        print(try_again)


    # elif len(player_choice) == 2:
    #     verb = player_choice[0]
    #     noun = player_choice[1]

# print(player_choice)
# objects[choice].look_object(current_room)

