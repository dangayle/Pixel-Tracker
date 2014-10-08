import json
from django.core import signing
from django.core.signing import BadSignature, SignatureExpired
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.dateparse import parse_datetime
from .signals import pixel_data
import logging
logger = logging.getLogger(__name__)



class PixelJSONSerializer(object):
    """Allows datetime.datetime encoding."""

    def dumps(self, obj):
        return json.dumps(obj, cls=DjangoJSONEncoder, separators=(',', ':'))

    def loads(self, obj):
        return json.loads(obj)


def dont_track(request):
    """Do not send tracking pixel when certain http headers exist."""

    http_x_purpose = request.META.get("HTTP_X_PURPOSE", "").strip().lower()
    http_x_moz = request.META.get("HTTP_X_MOZ", "").strip().lower()
    prefetch_qs_arg = request.GET.get("prefetch", None)
    dnt = int(request.META.get("HTTP_DNT", 0))
    return bool(
        any(x in http_x_purpose for x in ("prerender", "preview", "instant")) or
        ("prefetch" in http_x_moz) or
        prefetch_qs_arg or
        dnt
    )


def decode_pixel(tracking_pixel):
    """Decode tracking pixel data and publish as Django signal."""

    pixel = None
    try:
        pixel = signing.loads(
            tracking_pixel, serializer=PixelJSONSerializer, max_age=10)
    except SignatureExpired:
        logger.exception("pixel expired")
    except BadSignature:
        logger.exception("pixel invalid")

    if pixel:
        pixel['timestamp'] = parse_datetime(pixel['timestamp'])
        pixel_data.send(sender='decode_pixel', pixel_data=pixel)
