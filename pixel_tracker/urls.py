from django.conf.urls import patterns, url
from .views import tracking_pixel


urlpatterns = patterns('',
    url(r'^(?P<tracking_pixel>.*?).png', tracking_pixel, name="tracking_pixel"),
)
