__author__ = 'Kevin Mooney'

from django.conf import settings
import time

# expects that settings has a LATENCY_MIDDLEWARE dictionary
# with a WAIT_TIME key, which is an integer.

WAIT_TIME = getattr(settings,"LATENCY_MIDDLEWARE", dict()).get("WAIT_TIME", 30)


class LatencyMiddleware(object):

    def process_response(self, req, response):
        response['X-Latency'] = "{time_val}s".format(time_val=WAIT_TIME)
        time.sleep(WAIT_TIME)
        return response
