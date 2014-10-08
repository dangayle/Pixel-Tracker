from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from .utils import decode_pixel


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@require_GET
def tracking_pixel(request, tracking_pixel):
    """Decode tracking pixel request, return 204 No Content HTTP header

    decode_pixel verifies authenticity of pixel and fires off a Django
    signal with the data encoded in the pixel url.

    Returns a 204 No Content http response to save bandwidth.
    """

    decode_pixel(tracking_pixel)
    return HttpResponse(status=204)
