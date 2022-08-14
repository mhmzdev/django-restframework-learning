import imp
import json
from django.http import JsonResponse


# Create your views here.
def home(request, *args, **kwargs):
    # request --> from HttpRequest(django) not from requests(python)

    body = request.body  # byte string of JSON data
    # we need to convert it from byte string to JSON

    data = {}  # this is actual object/json/dict etc.
    try:
        data = json.loads(body) # json serialization
    except:
        pass
    
    data['params'] = dict(request.GET) # getting the query params http://localhost:8000/home/?some_key=some_value
    data['headers'] = dict(request.headers) # headers needs to be json serialize here
    data['content_type'] = request.content_type

    return JsonResponse(data)
