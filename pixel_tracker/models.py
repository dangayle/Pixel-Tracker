from pprint import pprint
from .signals import pixel_data


def simple_receiver(**kwargs):
    """Example receiver for pixel_data."""
    pixel_data = kwargs['pixel_data']
    pprint(kwargs)

pixel_data.connect(simple_receiver)
