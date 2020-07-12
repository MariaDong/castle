class Object():
    """Model an object in-game"""
    def __init__(
        self,
        slug,
        # An abbreviated name for the object.
        description,
        # Description given during 'look' method.
        text_in_room = '',
        can_pickup=True,
        # Specifies whether the object can be picked up.
        use_with='',
        # Specifies what other objects with object can be used with. 
        use_text='',
        # Specifies what text is displayed with this object is used via
        # the use_object method.
        updated_description = '',
        # Updated description, needed if object changes after use.
        cant_pickup_text = "You can't pick that up.",
        # Set to a default, can be customized for specific instances.
        ):
        self.slug = slug
        self.description = description
        self.can_pickup = can_pickup
        self.use_with = use_with
        self.use_text = use_text
        self.updated_description = updated_description
        self.cant_pickup_text = cant_pickup_text
        self.text_in_room = text_in_room
        """Initializes an instance of class Object. Must provide a slug
        name and the object's descript for the 'look' function. Objects
        can be picked up by default."""

    def add_dict(self, all_objects):
        """Adds the object to the global all_objects dictionary."""
        all_objects[self.slug] = self
        
    def look_object(self, player_inventory, current_room):
        """Checks if the object is in the current_room or in the player's
        inventory. If it is, prints the object's description."""
        if self.slug in current_room.room_inventory.keys():
            print(f"\t{self.description}")
        elif self.slug in player_inventory.keys():
            print(f"\t{self.description}")
        else:
            print(f"\tYou don't see a {self.slug}.")
    
    def pickup_object(self, player_inventory, current_room):
        """Checks if object is available to be picked up; if so, adds to
        player_inventory and removed from room_inventory."""
        if self.can_pickup == False:
            print(self.cant_pickup_text)
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
    
    # def check_object(self, player_inventory, current_room):
    #     if self.can_pickup == True and self.slug not in player_inventory.keys():
    #         print(f"You're not holding a {self.slug}")
    #     elif self.can_pickup == False and self.slug not in current_room.room_inventory.keys():
    #         print(f"You don't see a {self.slug}.")
    #     else:
    #         pass
        # elif self.use_alone == False:
        #     use_choice = input('What do you want to use this on?')
        #     if use_choice == self.use_with.Object.slug:
        #         print(self.use_with_text)
        #     if self.updated_description_with:
        #         self.description = self.updated_description_with
        #     if self.use_with.Object.updated_description_with:
        #         self.use_with.Object.description = self.use_with.Object.updated_description_with
        #         self.description = self.updated_description_alone

# class Door(Object):
#     """Model an door or other portal in-game"""
#     def __init__(self, all_objects, slug, description, locked=False, can_pickup=False):
#         super().__init__(slug, all_objects, description, can_pickup=False)
#         self.locked = locked
    
class Room():
    """Model for a room or area tile in-game"""
    def __init__(self, slug, entry_text, description, room_inventory={}):
        self.slug = slug
        self.entry_text = entry_text
        self.description = description
        self.room_inventory = room_inventory

    def enter_room(self, current_room):
        print(self.entry_text)
        current_room = self
    
    def look_room(self, current_room):
        if current_room == self:
            print(self.description)
            # for item in self.room_inventory.objects():
            #     print[item.slug]
        else: 
            print("You can't see that room from here.")
    
    def stage_item(self, all_objects, staged=[]):
        for stage in staged:
            all_objects[stage.slug] = stage
            self.room_inventory[stage.slug] = stage.__dict__
    
    def print_inventory(self):
        print(self.room_inventory.keys())
    
    def print_inventory_long(self):
        print(self.room_inventory.items())

