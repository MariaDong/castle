class Object():
    """Model an object in-game"""
    def __init__(
        self,
        slug,
        # An abbreviated name for the object.
        description,
        # Description given during 'look' method.
        text_in_room = '',
        # Text added to room description
        can_pickup=False,
        # Specifies whether the object can be picked up.
        can_use = False,
        # Specifies whether an object can be used at all.
        use_with='',
        # Specifies what other objects with object can be used with.
        use_alone=False,
        # Specifies if the object can be used alone.
        only_in_room = [],
        # Specifies if there is a specific room that the item has to 
        # be used in and what the updated text would be.
        use_text='',
        # Specifies what text is displayed with this object is used via
        # the use_object method.
        used=False,
        # Flag updated after object is used.
        updated_description = '',
        # Updated description, needed if object changes after use.
        cant_pickup_text = "You can't pick that up.",
        # Set to a default, can be customized for specific instances.
        ):
        self.slug = slug
        self.description = description
        self.text_in_room = text_in_room
        self.can_pickup = can_pickup
        self.can_use = can_use
        self.use_with = use_with
        self.use_alone = use_alone
        self.only_in_room = only_in_room
        self.use_text = use_text
        self.used = used
        self.updated_description = updated_description
        self.cant_pickup_text = cant_pickup_text
        self.text_in_room = text_in_room


    def __str__(self):
        return self.slug
        
    def look_object(self, player_inventory, current_room):
        print(f"\n\t{self.description}")
    
    def pickup_object(self, player_inventory, current_room):
        """Checks if object is available to be picked up; if so, adds to
        player_inventory and removed from room_inventory."""
        if self.can_pickup == False:
            print(self.cant_pickup_text)
        elif self in player_inventory:
            print(f"The {self.slug} is already in your inventory.")
        else:
            print(f"You put the {self.slug} into your inventory.")
            player_inventory.append(self)
            current_room.room_inventory.remove(self)
    
    def drop_object(self, player_inventory, current_room):
        if self in player_inventory:
            print(f"\n\tYou drop the {self.slug} on the ground.")
            current_room.room_inventory.append(self)
            player_inventory.remove(self)
            self.text_in_room = f"There is a {self.slug} on the ground."
    
    def use_object(self, current_room, paired=''):
        if not paired:
            if self.use_alone = True:
                if 
                print(self.use_text)
        if paired == self.use_with
        print(self.use_text)
    
    def used_with(self,paired):
        print(self.use_text)
    
    # def use_with_object(self):
    #     if self.updated_description:
    #         self.description = self.updated_description

# class Door(Object):
#     """Model an door or other portal in-game"""
#     def __init__(self, all_objects, slug, description, locked=False, can_pickup=False):
#         super().__init__(slug, all_objects, description, can_pickup=False)
#         self.locked = locked
    
class Room():
    """Model for a room or area tile in-game"""
    def __init__(self, slug, entry_text, description, room_inventory=[]):
        self.slug = slug
        self.entry_text = entry_text
        self.description = description
        self.room_inventory = room_inventory

    def enter_room(self, current_room):
        print(self.entry_text)
        current_room = self
    
    def look_room(self, current_room):
        if current_room == self:
            room_description = self.description
            for item in self.room_inventory:
                room_description += item.text_in_room
            print(f"\n\t{room_description}")
        else:
            print("You can't see that room from here.")
    
    def stage_item(self, staged=[]):
        for stage in staged:
            self.room_inventory.append(stage)
    
    # def print_inventory(self):
    #     print(self.room_inventory)
    
    # def print_inventory_long(self):
    #     print(self.room_inventory.items())
    
    def __str__(self):
        return self.slug