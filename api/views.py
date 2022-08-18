import imp
import json
from turtle import title
from django.http import JsonResponse
from products.models import Product


# Create your views here.
def home(request, *args, **kwargs):
    # request --> from HttpRequest(django) not from requests(python)

    body = request.body  # byte string of JSON data
    # we need to convert it from byte string to JSON

    data = {}  # this is actual object/json/dict etc.
    try:
        data = json.loads(body)  # json serialization
    except:
        pass

    # getting the query params http://localhost:8000/home/?some_key=some_value
    data['params'] = dict(request.GET)
    # headers needs to be json serialize here
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)


def products(request, *args, **kwargs):

    product_model = Product(
        title='some title', content='Some content here', price=10.12)

    data = {}

    if product_model:
        data['id'] = product_model.id
        data['title'] = product_model.title
        data['context'] = product_model.content
        data['price'] = product_model.price

    return JsonResponse(data)
