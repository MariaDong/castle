class Object():
    """Model an object in-game"""
    def __init__(self, current_room, slug, description, can_pickup=True):
        self.slug = slug
        self.description = description
        self.can_pickup = can_pickup
        
    def look_object(self, current_room, player_inventory):
        if self in current_room.room_inventory:
            print(self.description)
        elif self in player_inventory:
            print(self.description)
        else:
            print(f"You don't see a {self.slug}.")
    
    # def pickup_object(self, player_inventory, current_room):
    #     if self.can_pickup == False:
    #         print("You can't pick that up.")
    #     elif self in player_inventory.keys():
    #         print(f"The {self.slug} is already in your inventory.")
    #     elif self != current_room:
    #         print(f"You don't see a {self.slug}.")
    #     else:
    #         print(f"You put the {self.slug} into your inventory.")
    #         player_inventory.append(self.slug)
    #         self.location = 'inventory'
    
class Room():
    """Model for a room or area tile in-game"""
    def __init__(self, slug, short, description, room_inventory={}):
        self.slug = slug
        self.short = short
        self.description = description

    def enter_room(self, current_room):
        print(self.short)
        current_room = self
    
    def look_room(self, current_room):
        if current_room == self:
            print(self.description)
        else: 
            print("You can't see that room from here.")
    
    def stage_item(self, room_contents, items):
        for item in items:
            room_contents[self.slug] = item
    
    def receive_dropped(self, room_contents, item):
        room_contents[{self.slug}] = item
        self.description += f'The following items have been dropped on the floor: {item}.'
    
    # def receive_item(self, item, objects):
    #     self.room_inventory[item]
    
    # def print_room_inventory(self):
    #     print(self.room_inventory)

