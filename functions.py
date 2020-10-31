"""This file contains most of the main functions used in the game. With
the get_command function, most of the functions run methods from the 
player Object or the item Objects. """

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

def stage_rooms(rooms_to_stage, items_to_stage):
    """Looks in staging.py for a list, rooms_to_stage, and a
    dictionary of items to stage in each room. Iterates over the list,
    calling the stage_items method from the Room."""
    while rooms_to_stage:
        currently_staging = rooms_to_stage.pop()
        print(f"Staging the {currently_staging}.")
        currently_staging.stage_items(staged=items_to_stage[currently_staging])

def pair_items(paired_items):
    for key, value in paired_items.items():
        key.use_with = value
        value.use_with = key

def player_inventory(player, inventory_message):
    """Prints the contents of the players inventory or advises empty."""
    print(inventory_message)
    if not player.inventory:
        print("\tYou don't have anything in your inventory.")
    else:
        item_list = []
        for item in player.inventory:
            item_list.append(item.slug.title())
            print(f"\n\t{item_list}")

def player_look_object(choice, player):
    """Checks to see if the object is in inventory or current room. If
    so, runs Player's look_object method"""
    found_item = False
    for item in player.inventory + player.current_room.room_inventory:
        if item.slug == choice[1]:
            found_item = True
            item.look_object()
    if found_item == False:
            print(f"You don't see a {choice[1]}.")

def player_take_object(choice, player):
    """Checks if object is in the room. If so, pulls into player
    inventory. If object not in player inventory on room inventory,
    give an error message."""
    found_item = False
    for item in player.inventory:
        if item.slug == choice[1]:
            found_item = True
            print(f"\n\tYou're already holding a {choice[1]}.")
    for item in player.current_room.room_inventory:
        if item.slug == choice[1]:
            found_item = True
            item.pickup_object(player)

    if found_item == False:
            print(f"\n\tYou don't see a {choice[1]}.")

def player_drop_object(choice, player):
    """Checks if object is in inventory. If so, drops into
    player.current_room's room_inventory."""
    found_item = False
    for item in player.inventory:
        if item.slug == choice[1]:
            found_item = True
            item.drop_object(player)
    if found_item == False:
            print(f"\n\tYou're not holding a {choice[1]}.")

def player_use_one(choice, player):
    """Checks if item is in player inventory or room. If found_item ==
    True, excutes item's use_it_alone method."""
    found_item = False
    for item in player.inventory + player.current_room.room_inventory:
        if item.slug == choice[1]:
            found_item = True
            item.use_it_alone(player)
    if found_item == False:
        print(f"\n\tYou don't see a {choice[1]} right now.")

def player_use_two(choice, player):
    """Checks if both items are in player inventory or room. If found_
    item_1 and found_item_2 are True, checks for use_text to assign the
    main item. Runs use_it_together method from main item and use_paired
    method from paired item."""
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
        item_1.use_together(item_2, player)