'''A file containing all of the in-game objects.'''

from class_models import Object

# The Object class. Default values for this have been provided below and can be
# copy-pasted and then uncommented as need.

# object_name = Object(
#         slug, 
#         description, 
#         can_pickup = True,
#         use_alone = False,
#         use_alone_text = '', 
#         use_with='',
#         use_with_text='',
#         updated_description_alone = '',
#         updated_description_with = '',
#         ):

candle = Object(
    'candle',
    "It's a small, red taper, about an inch long. It appears brand new.",
    use_with = 'candle',
    use_with_text = """The match flares to life. You hold it to the tip of the
    candle. After a moment, the room fills with an odd scent, earthy and floral
    and just a bit like hot metal. It's unnerving, and you wonder what the 
    thing is made out of.""",
    updated_description_with = """It's a small, red taper, about an inch long.
    A tiny flame gutters on the end of it."""
    )

match = Object(
    'match',
    """A solitary match. The head is white, which you haven't seen in a while.
    It reminds you of the stories of men and women going mad from phosophorus
    poisoning, but it's the only match you can see.""",
    use_alone = True,
    use_alone_text= """You consider striking it, but as it's your only match,
    you decide to wait until you figure out what to use it with.""",
    use_with = 'candle',
    use_with_text= """The match flares to life. You hold it to the tip of the
    candle. After a moment, the room fills with an odd scent, earthy and floral
    and just a bit like hot metal. It's unnerving, and you wonder what the 
    thing is made out of.""",
    updated_description_with="""A burnt-out match. It's worthless."""
)