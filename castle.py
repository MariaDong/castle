"""A simple text adventure game"""

#-----------1.0 INITIALIZE OBJECTS, ROOMS, AND MESSAGES.----------------

# Initialize player variables.
player_inventory = []
player_map = []

# Import modules to model rooms and objects.
from time import sleep
from class_models import *
from rooms import *

# Import the objects used in the game.
from objects import *
# Call stage item method to move objects to the correct rooms.
parlor.stage_item(staged=[candle, match, bell])

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

def get_command():
    """Asks the player for their next move and sanitizes the input."""
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
            noun = input("\n\tUse what?\t")
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
        return 'mistaken'

# Start the main game loop.
while True:
    choice = get_command()
    if choice[0] == 'inventory':
        print(inventory_message)
        if not player.inventory:
            print("\tYou don't have anything in your inventory.")
        else:
            item_list = []
            for item in player.inventory:
                item_list.append(item.slug.title())
                print(f"\n\t{item_list}")

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

    if choice[0] == 'look' or choice[0] == 'examine':
        if choice[1] == 'room' or choice[1] == player.current_room.slug:
            player.look_room()
        else:
            found_item = False
            for item in player.inventory + player.current_room.room_inventory:
                if item.slug == choice[1]:
                    found_item = True
                    item.look_object()
            if found_item == False:
                    print(f"You don't see a {choice[1]}.")

# The take command behaves in a similar fashion and executes the
# pickup_object method from Object and adds to player inventory.

    elif choice[0] == 'take' or choice[0] == 'pick' or choice[0] == 'pickup':
        found_item = False
        for item in player.inventory + player.current_room.room_inventory:
            if item.slug == choice[1]:
                found_item = True
                item.pickup_object(player)
        if found_item == False:
                print(f"\n\tYou don't see a {choice[1]}.")

# The drop command works the same, executing the drop_object method.

    elif choice[0] == 'drop':
        found_item = False
        for item in player.inventory:
            if item.slug == choice[1]:
                found_item = True
                item.drop_object(player)
        if found_item == False:
                print(f"\n\tYou're not holding a {choice[1]}.")

# The 'use' command triggers a series of actions depending on how many
# nouns were entered.

    elif choice[0] == 'use':
        # If player has only entered one noun to use, check if item is 
        # available, and if so, run the use_it_alone method from Object.
        if len(choice) == 2:
            found_item = False
            for item in player.inventory + player.current_room.room_inventory:
                if item.slug == choice[1]:
                    found_item = True
                    item.use_it_alone(player)
            if found_item == False:
                print(f"\n\tYou don't see a {choice[1]} right now.")
        # if player has entered 2 nouns, check if items are both available.)
        elif len(choice) == 3:
            found_item_1 = False
            found_item_2 = False
            for item in player.inventory + player.current_room.room_inventory:
                if item.slug == choice[1]:
                    found_item_1 = True
                    item_1 = item
                if item.slug == choice[2]:
                    found_item_2 = True
                    item_2 = item
            # Stop if one of the items is missing.
            if found_item_1 == False:
                print(f"\n\tYou don't see a {choice[1]}.")
            elif found_item_2 == False:
                print(f"\n\tYou don't see a {choice[2]}.")
            # If both items are present, check for Object.use_text, which 
            # will indicate which item is the "main item". Use the
            # use_together method from the object, which will also return
            # True if the two objects are paired correctly and False if
            # the objects are not paired correctly. If true, run the
            # use_paired method on the secondary object to update used
            # status and descrption.
            elif item_1 and item_2:
                pairing = False
                if item_1.use_text:
                    pairing = item_1.use_together(item_2, player)
                    if pairing == True:
                        item_2.use_paired()
                else:
                    pairing = item_2.use_together(item_1, player)
                    if pairing == True:
                        item_1.use_paired()
        else:
            print("\n\tThese are too many objects to use together.")
    # establish a pass at end of loop in case no conditions are met.
    else: 
        print(try_again)
