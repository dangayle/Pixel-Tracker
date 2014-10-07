import datetime
from django import template
from django.core import signing
import logging
from ..utils import PixelJSONSerializer, dont_track

logger = logging.getLogger(__name__)
register = template.Library()


@register.inclusion_tag('pixel.html', takes_context=True)
def pixel(context):
    """Generate tracking pixel for single object."""

    pixel = None
    if context.get('object', None):
        data = {
            "path": context['request'].get_full_path(),
            "content_type": context['object'].__class__.__name__,
            "content_id": context['object'].id,
            "timestamp": datetime.datetime.now()
        }
        pixel = signing.dumps(
            data, serializer=PixelJSONSerializer, compress=True)

    if dont_track(context['request']):
        pass
    else:
        return {
            'pixel_url': pixel
        }
