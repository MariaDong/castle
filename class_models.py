class Object():
    """Model an object in-game"""
    def __init__(
        self, 
        all_objects,
        slug, 
        description, 
        can_pickup=True,
        use_alone=False,
        use_alone_text = '', 
        use_with='',
        use_with_text='',
        updated_description_alone = '',
        updated_description_with = '',
        ):
        self.slug = slug
        self.description = description
        self.can_pickup = can_pickup
        self.use_alone = use_alone
        self.use_alone_text = use_alone_text
        self.updated_description_alone = updated_description_alone
        self.use_with = use_with
        self.use_with_text = use_with_text
        self.updated_description_with = updated_description_with
        all_objects[self.slug] = self
        
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
    
    def use_object(self, player_inventory, current_room):
        if self.can_pickup == True and self.slug not in player_inventory.keys():
            print(f"You're not holding a {self.slug}")
        elif self.can_pickup == False and self.slug not in current_room.room_inventory.keys():
            print(f"You don't see a {self.slug}.")
        elif self.use_alone == False:
            use_choice = input('What do you want to use this on?')
            if use_choice == self.use_with.Object.slug:
                print(self.use_with_text)
            if self.updated_description_with:
                self.description = self.updated_description_with
            if self.use_with.Object.updated_description_with:
                self.use_with.Object.description = self.use_with.Object.updated_description_with
                
        else:
            print(self.use_alone_text)
            if self.updated_description_alone:
                self.description = self.updated_description_alone

class Door(Object):
    """Model an door or other portal in-game"""
    def __init__(self, all_objects, slug, description, locked=False, can_pickup=False):
        super().__init__(slug, all_objects, description, can_pickup=False)
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
    
    def stage_item(self, staged):
        self.room_inventory[staged.slug] = item.__dict__
    
    def print_inventory(self):
        print(self.room_inventory)

