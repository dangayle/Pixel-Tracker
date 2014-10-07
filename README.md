Django Pixel Tracker
==============

Django tracking pixel for content analytics.

Django Pixel Tracker uses Django signals to publish data about single object views. You can use this data for internal and external use, such as:

* In-house analytics tracking
* "Most active" stories/blogposts/etc


Installation
------------

Add `pixel_tracker` to your installed apps:

```python
INSTALLED_APPS = (
    ...,
    'pixel_tracker',
    ...
)
```

Add `tracking_pixel` to your site urls:

```python
urlpatterns = patterns('',
    ...,
    (r'^pixel/', include('pixel_tracker.urls')),
    ...,
)
```

Add pixel to your templates:


```html
{% load pixel %}
<html>
    <head></head>
    <body>
        {% pixel %}
    </body>

</html>
```


Usage
-----

To use Django Pixel Tracker, you need create a receiver to subscribe to the `pixel_data` signal within your app. Example:

```python
from pixel_tracker.models import pixel_data

def simple_receiver(**kwargs):
    pixel_data = kwargs['pixel_data']
    pprint(pixel_data)

pixel_data.connect(simple_receiver)
```

In this example, it will simply print out the pixel data as a Python Dict, but you could store this data in your database, load it into Redis or send off a Celery task. What you do with it is up to you.

The default data that it collects is:

* Name of object model
* PK of object item
* Full url path of the request
* Timestamp

You could extend that with any data that is available in the context.
