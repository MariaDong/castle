#Initialize dictionaries, lists, etc., that are needed for our game to function.
objects = {}
player_inventory = []
# from class_models import Object
from class_models import Room
from class_models import Object

room_contents = {}
living_room = Room(
    'living room', 
    'You enter a small living room.',
    'The living room is richly upholstered with many pieces of furniture. A small candle sits on a table.',
)
from objects import candle
living_room.stage_item(room_contents, ['candle'])
current_room = living_room
"""Initialize the current_room variable and set it to the recently created living_room"""
living_room.enter_room(current_room)
# candle = Object(current_room, 'candle','It is a small, red taper, about an inch long. It does not appear to be lit.')
living_room.stage_item(room_contents, 'candle')

print(room_contents['living room'])

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
