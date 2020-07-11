class Object():
    """Model an object in-game"""
    def __init__(self, object_dict, slug, description, can_pickup=True):
        self.slug = slug
        self.description = description
        self.can_pickup = can_pickup
        object_dict[self.slug] = self

    def look_object(self, player_inventory, current_room):
        if self.slug in current_room.room_inventory.keys():
            print(self.description)
        elif self in player_inventory:
            print(self.description)
        else:
            print(f"You don't see a {self.slug}.")
    
    def pickup_object(self, player_inventory, current_room):
        if self.can_pickup == False:
            print("You can't pick that up.")
        elif self.slug in player_inventory.keys():
            print(f"The {self.slug} is already in your inventory.")
        elif self.slug not in current_room.room_inventory.keys():
            print(f"You don't see a {self.slug}.")
        else:
            print(f"You put the {self.slug} into your inventory.")
            player_inventory[self.slug] = self.__dict__
            del current_room.room_inventory[self.slug]
    
    def drop_object(self, player_inventory, current_room):
        if self.slug in player_inventory.keys():
            print(f"Your drop the {self.slug} on the ground.")
            current_room.room_inventory[self.slug] = self.__dict__
            del player_inventory[self.slug]

class Door(Object):
    """Model an door or other portal in-game"""
    def __init__(self, object_dict, slug, description, locked=False, can_pickup=False):
        super().__init__(slug, object_dict, description, can_pickup=False)
        self.locked = locked
    
class Room():
    """Model for a room or area tile in-game"""
    def __init__(self, slug, entry_text, description, add_items=[], room_inventory={}):
        self.slug = slug
        self.entry_text = entry_text
        self.description = description
        self.room_inventory = room_inventory
        for Object in add_items:
            self.room_inventory[Object.slug] = Object.__dict__

    def enter_room(self, current_room):
        print(self.entry_text)
        current_room = self
    
    def look_room(self, current_room):
        if current_room == self:
            print(self.description)
        else: 
            print("You can't see that room from here.")
    
    def stage_item(self, item):
        self.room_inventory[item.slug] = item.__dict__
    
    def print_inventory(self):
        print(self.room_inventory)


