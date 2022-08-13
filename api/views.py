import imp
from django.http import JsonResponse

# Create your views here.
def home(request, *args, **kwargs):
    return JsonResponse(
        {
            "message": "You are doing great so far!"
        }
    )