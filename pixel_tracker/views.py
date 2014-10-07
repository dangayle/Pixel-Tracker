from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from .utils import decode_pixel
import logging

logger = logging.getLogger(__name__)
TRANSPARENT_1_PIXEL_GIF = "\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\xff\xff\xff\x00\x00\x00\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b"


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@require_GET
def tracking_pixel(request, tracking_pixel):
    decode_pixel(tracking_pixel)
    return HttpResponse(TRANSPARENT_1_PIXEL_GIF, content_type='image/gif')
