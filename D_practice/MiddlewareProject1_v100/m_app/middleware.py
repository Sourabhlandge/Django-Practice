from django.shortcuts import HttpResponse
class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        print('This Line Printed at pre processing request')
        response = self.get_response(request)
        print('This LIne printed at post processing request')
        return response
class AppmaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        return HttpResponse('<h1>This Website under Maintenance..Please Try After 2pm Thank You..</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        response = self.get_response(request)
        return response
    def process_exception(self,request,exception):
        message = '<h1>Currently We are Facing Some Technical Problem ,please try After Some Time <hr></h1>'
        message2 = '<h2>Raised Exception:{}</h2>'.format(exception.__class__.__name__)
        message3 = '<h2>Exception Description/Message:{}</h2>'.format(exception)
        return HttpResponse(message+message2+message3)
class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        print('This Line Printed by First Middleware at pre processing request')
        response = self.get_response(request)
        print('This LIne printed by First Middleware at post processing request')
        return response
class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        print('This Line Printed by Second Middleware at pre processing request')
        response = self.get_response(request)
        print('This LIne printed by Second Middleware at post processing request')
        return response

class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self, request):
        print('This Line Printed by Third Middleware at pre processing request')
        response = self.get_response(request)
        print('This LIne printed by Third Middleware at post processing request')
        return response