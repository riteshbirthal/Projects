from django.shortcuts import HttpResponse

class CustomMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        print(request.user, response)
        # if str(request.user)=='Admin' and request.path=='/cart/':
        #     return HttpResponse("Sorry! You cannot place order. You're Admin.")
        return response
    
    def process_view(request, *args, **kwargs):
        # return HttpResponse("Hello")
        print("Before Middleware: ", request)
        return None