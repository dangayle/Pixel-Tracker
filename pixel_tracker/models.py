from pprint import pprint
from django.dispatch import receiver
from .signals import pixel_data


@receiver(pixel_data)
def example_receiver(**kwargs):
    """Example receiver of pixel_data signal."""

    pixel_data = kwargs['pixel_data']
    pprint(pixel_data)
