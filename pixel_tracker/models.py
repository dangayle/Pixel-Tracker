from pprint import pprint
from django.dispatch import receiver
from .signals import pixel_data
from .tasks import pretty_print_tracking_data


@receiver(pixel_data)
def example_receiver(**kwargs):
    """Example receiver for pixel_data."""

    pixel_data = kwargs['pixel_data']
    pprint(pixel_data)
