from pprint import pprint
from django.dispatch import Signal

pixel_data = Signal(providing_args=["pixel_data"])
