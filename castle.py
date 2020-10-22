"""A simple text adventure game"""

#-----------1.0 INITIALIZE OBJECTS, ROOMS, AND MESSAGES.----------------

# Initialize player variables.
player_inventory = []
player_map = []

# Import modules to model rooms and objects.
from time import sleep
from class_models import Object
from class_models import Room

# Import the rooms used in the game.
from rooms import *
current_room = parlor
# Import the objects used in the game.
from objects import *
# Call stage item method to move objects to the correct rooms.
parlor.stage_item(staged=[candle, match])

# Initialize stock messages used in while loop - these are constant and do not
# change through the game.
try_again = "\n\tI don't think I understood that. Maybe tell me a different way?"
inventory_message = "\n\tHere are the things in your inventory. Use LOOK to "
inventory_message +="examine any of them closer."
help_message = """\n\tHere is a list of commands you can use: MAP, INVENTORY, 
LOOK, TAKE, USE."""

# The get_command function asks the player what they want to do and sanitizes
# the input so that it can be processed by the while loop.

def get_command():
    """Asks the player for their next move."""
    # Prompt player for a command and store as a string.
    choice = input('\nWhat do you want to do?\t\t')
    # Sanitize input:
    # Remove whitespace and split the choice string into a lowercase list.
    player_choice = choice.strip().lower().split()
    # Delete 'up', 'at', 'with', 'on', 'the', to make player_choice list easier
    # to process.
    remove_from_choices = ['up', 'at', 'with', 'on', 'the']
    for word in remove_from_choices:
        if word in player_choice:
            player_choice.remove(word)
    # Assign first item in player_choice to the 'verb' variable, then get a 
    # second parameter ("noun") if needed.
    verb = player_choice[0]
    one_word_commands=['inventory','help']
    two_word_commands=['look', 'examine', 'take', 'pick','pickup', 'drop']
    if verb in one_word_commands:
        return [verb]
    elif len(player_choice) == 2 and verb in two_word_commands:
        noun = player_choice[1]
        return [verb, noun]
    elif len(player_choice) == 1 and verb in two_word_commands:
        if verb in ['look']:
            noun = input(f"\n\t\t{verb.title()} at what?\t")
        else:
            noun = input(f"\n\t\t{verb.title()} what?\t")
        return [verb, noun]
    elif verb == 'use':
        if len(player_choice) == 1:
            noun = input("Use what?")
            return [verb, noun]
        elif len(player_choice) == 2:
            noun = player_choice[1]
            return [verb, noun]
        elif len(player_choice) == 3:
            noun = player_choice[1]
            noun_2 = player_choice[2]
            return [verb, noun, noun_2]
        else:
            print(try_again)
    else:
        print(try_again)

# Greet the player.

# Start the main game loop.
while True:
    choice = get_command()
    if choice[0] == 'inventory':
        print(inventory_message)
        if not player_inventory:
            print("\tYou don't have anything in your inventory.")
        else:
            for item in player_inventory:
                print(item)

    # If the player chooses 'help', a list of commands is printed.
    elif choice[0] == 'help':
        print(help_message)

    # If the verb is 'look' or 'examine', check first to see if the
    # item is 'room' or is the slug from the current room. If so, 
    # call the look_room method on the current room. If not, set a flag
    # for found_item to False. Run through the objects in player_inventory
    # and in the current_room.room_inventory and see if the slugs of any
    # of the objects match. If they do, set the found_item flag to True
    # and call the look_object method on the object. If the object is 
    # not found, report that the player cannot see it.

    elif choice[0] == 'look' or choice[0] == 'examine':
        if choice[1] == 'room' or choice[1] == current_room.slug:
            current_room.look_room(current_room)
        else:
            found_item = False
            for item in player_inventory + current_room.room_inventory:
                if item.slug == choice[1]:
                    found_item = True
                    item.look_object(player_inventory, current_room)
            if found_item == False:
                    print(f"You don't see a {choice[1]}.")

    # The take command behaves in a similar fashion and executes the
    # pickup_object method from Object instance.

    elif choice[0] == 'take' or choice[0] == 'pick' or choice[0] == 'pickup':
        found_item = False
        for item in player_inventory + current_room.room_inventory:
            if item.slug == choice[1]:
                found_item = True
                item.pickup_object(player_inventory, current_room)
        if found_item == False:
                print(f"\n\tYou don't see a {choice[1]}.")

    # The drop command works the same, executing the drop_object method.

    elif choice[0] == 'drop':
        found_item = False
        for item in player_inventory:
            if item.slug == choice[1]:
                found_item = True
                item.drop_object(player_inventory, current_room)
        if found_item != True:
                print(f"\n\tYou're not holding a {choice[1]}.")


#     # The use object command requires two objects that are used together.
#     # Each object is first checked with the check_object method to make sure
#     # is it being held by the player and it is something that can be used.
#     elif verb =='use':
#         if len(player_choice) > 3:
#             print(try_again)
#         elif len(player_choice) == 1:
#             first_noun = input ('Use what?')
#             second_noun = input ('With What?')
#         elif len(player_choice) == 2:
#             second_noun = input ('With What?')


#             # if first_noun in all_objects.keys():
#             #     second_noun = input ('With What?'):
#             #     if second_noun in all_objects.keys():

#     # The following commands are for troubleshooting only.
#     elif verb == 'inventory_long':
#         print(player_inventory)
#     elif verb == 'room_inventory':
#         current_room.print_inventory()
#     elif verb == 'room_inventory_long':
#         current_room.print_inventory_long()
#     # Finally, an 'else' to capture any misunderstood commands.
#     else:
#         print(try_again)


#     # elif len(player_choice) == 2:
#     #     verb = player_choice[0]
#     #     noun = player_choice[1]

# # print(player_choice)
# # objects[choice].look_object(current_room)

