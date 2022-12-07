from rest_framework import throttling
from configs import variable_system as vr_sys
from helpers.response import *
from rest_framework.views import exception_handler

class CustomThrottle(throttling.SimpleRateThrottle):
    def parse_rate(self, rate):
        if rate is None:
            return (None, None)
        num, period = rate.split(vr_sys.THROTTLING['split'])
        num_requests = int(num)
        duration = {vr_sys.THROTTLING['per_time'][-1]: int(vr_sys.THROTTLING['per_time'][:-1])}[period[0]]
        return (num_requests, duration)
    
    def allow_request(self, request, view):
        if request.method in vr_sys.THROTTLING['method']:
            return True
        return super().allow_request(request, view)
    
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return response
    else:
        response = exc.detail
    return response_data(message=response)
    
class UserThrottle(CustomThrottle, throttling.UserRateThrottle):
    rate = vr_sys.THROTTLING['rate'] + vr_sys.THROTTLING['split'] + vr_sys.THROTTLING['per_time'][-1]
    