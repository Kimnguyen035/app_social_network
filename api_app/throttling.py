from rest_framework.throttling import UserRateThrottle,SimpleRateThrottle
from configs import variable_system as vr_sys
from helpers.response import *

class CustomThrottle(SimpleRateThrottle):
    def parse_rate(self, rate):
        if rate is None:
            return (None, None)
        num, period = rate.split(vr_sys.THROTTLING['split'])
        num_requests = int(num)
        duration = {vr_sys.THROTTLING['per_time'][-1]: vr_sys.THROTTLING['per_time'][:-1]}[period[0]]
        return (num_requests, duration)
    
    def allow_request(self, request, view):
        if request.method in vr_sys.THROTTLING['method']:
            return True
        return super().allow_request(request, view)
    
def custom_exception_handler(exc, context):
    return response_data(message=exc.detail)
    
class UserThrottle(CustomThrottle, UserRateThrottle):
    rate = vr_sys.THROTTLING['rate'] + vr_sys.THROTTLING['split'] + vr_sys.THROTTLING['per_time']
    