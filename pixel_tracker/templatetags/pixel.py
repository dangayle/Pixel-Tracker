import datetime
from django import template
from django.core import signing
from ..utils import PixelJSONSerializer, dont_track

register = template.Library()


@register.inclusion_tag('pixel.html', takes_context=True)
def pixel(context):
    """Generate tracking pixel for single object.

    Context data is encoded as a url-safe, signed, timestamped hash value
    that is then used as the url for a png image request (see views.py).

    Function is set to respect a browser's "Do Not Track" setting.
    """

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
