from class_models import Object

# The minimum call for an object is: (slug, description, text_in_room). 
# By default, can_pickup, can_use, and use_alone are set to False.

# All option available, in order, include slug, description, 
# text_in_room, can_pickup, can_use, use_with, use_alone, only_in_room, 
# use_text, used, updated_description, cant_pickup_text

candle = Object(
    'candle',
    "It's a small, red taper, about an inch long. It appears brand new.",
    "There's a candle in the center of the table.",
    can_pickup = True,
    can_use = True,
    use_with = 'match',
    use_text = """The match flares to life. You hold it to the tip of the
    candle. After a moment, the room fills with an odd scent, earthy and floral
    and just a bit like hot metal. It's unnerving, and you wonder what the 
    thing is made out of.""",
    updated_description = """It's a small, red taper, about an inch long.
    A tiny flame gutters on the end of it."""
    )

match = Object(
    'match',
    """A solitary match. The head is white, which you haven't seen in a while.
    It reminds you of the stories of men and women going mad from phosophorus
    poisoning, but it's the only match you can see.""",
    "You think you see a match.",
    can_pickup = True,
    can_use = True,
    updated_description="""A burnt-out match. It's worthless."""
)

bell = Object (
    'bell',
    """A small, golden bell.""",
    "There's a bell on the floor.",
    can_pickup = True,
    can_use = True,
    use_alone = True,
    use_text= """You ring the bell. The sound bounces through the room, 
    but nothing happens.""",
    only_in_room = ['stoop', "The door swings open."]
)
