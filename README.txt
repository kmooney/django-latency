==============
django-latency
==============

django-latency is a django application that only contains middleware to simulate network
latency on your local machine.  It causes your views to take several seconds to return.

This helps you identify client-side code that relies on low-latency server side code,
which is generally an anti-pattern.

Like a runner training with weighted shoes, django-latency lets you feel the pain of 
client-server dependencies.  


Set Up
=================
Setting up django-latency is easy.  After it is installed in your environemnt and on 
your path, simply add the middleware class to your MIDDLEWARE_CLASSES list::

    MIDDLEWARE_CLASSES = (
        ...
        'latency.middleware.LatencyMiddleware',
        ...
    )

django-latency optionally accepts a settings variable called LATENCY_MIDDLEWARE.  Currently, 
LATENCY_MIDDLEWARE is a dictionary whose only key is "WAIT_TIME," a floating point value.

For example::

    LATENCY_MIDDLEWARE = {
        'WAIT_TIME': 5.0
    }
