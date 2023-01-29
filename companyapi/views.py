# import packages
from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home Page Published")
    friends = ['prabhi',
                'bhuvnesh',
                'muskan']
    return JsonResponse(friends, safe = False)