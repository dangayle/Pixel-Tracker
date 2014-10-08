from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.views.decorators.cache import cache_control
from .utils import decode_pixel


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@require_GET
def tracking_pixel(request, tracking_pixel):
    decode_pixel(tracking_pixel)
    return HttpResponse(status=204)
