from class_models import Object
candle = Object(
    'candle',
    "It's a small, red taper, about an inch long. It appears brand new.",
    use_with = 'candle',
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
    use_with = 'candle',
    use_text= """The match flares to life. You hold it to the tip of the
    candle. After a moment, the room fills with an odd scent, earthy and floral
    and just a bit like hot metal. It's unnerving, and you wonder what the 
    thing is made out of.""",
    updated_description="""A burnt-out match. It's worthless."""
)

test_object = Object(
    'test_object',
    'used for testing',
    use_with = 'test-object 2',
    use_text = 'use-text',
    updated_description = 'updated-description',
)