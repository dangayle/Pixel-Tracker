from pprint import pprint
from django.dispatch import Signal

pixel_data = Signal(providing_args=["pixel_data"])


def simple_receiver(**kwargs):
    pixel_data = kwargs['pixel_data']
    pprint(kwargs)


pixel_data.connect(simple_receiver)
