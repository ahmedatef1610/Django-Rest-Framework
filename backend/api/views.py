import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """

    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        data = serializer.data
        print(instance)
        print(data)
        return Response(data)
    return Response({"invalid": "not good data"}, status=400)



###########################################################################################################################################################
###########################################################################
# 8

###########################################################################
# 7
# @api_view(['POST'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """

#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         instance = serializer.save();
#         data = serializer.data
#         print(instance)
#         print(data)
#         return Response(data)
#     return Response({"invalid": "not good data"}, status=400)
###########################################################################
# 6
# @api_view(['POST'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """
#     print(request.POST)
#     print(request.data)

#     instance = Product.objects.all().order_by("?").first()
#     instance = Product.objects.all().last()
#     data = {}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)
###########################################################################
# 5
# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """


#     model_data = Product.objects.all().order_by("?").first()
#     model_data = Product.objects.all().last()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
#     return Response(data)
###########################################################################
# 4
# @api_view(['GET', 'POST'])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API VIEW
#     """

#     if request.method != "POST":
#         return Response({"detail": "GET not allowed"}, status=405)

#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return Response(data)
###########################################################################
# 3
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)
###########################################################################
# 2
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         # data['id'] = model_data.id
#         # data['title'] = model_data.title
#         # data['content'] = model_data.content
#         # data['price'] = model_data.price

#         # model instance (model_data)
#         # turn a Python dict
#         # return JSON to my client
#         # data = model_to_dict(model_data)
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#         print(data) # {'id': 4, 'title': 'Hello world', 'price': Decimal('0.00')}
#         json_data_str = json.dumps(data)
#     # return JsonResponse(data)
#     return HttpResponse(json_data_str, headers={"content-type":"application/json"})

###########################################################################
# 1
# def api_home(request, *args, **kwargs):
#     # request -—> HttpRequest -—> Django
#     # print(dir(request))
#     # request.body
#     body = request.body # byte string of JSON data
#     print(body)

#     data = {}
#     try:
#         data = json.loads(body) # string of JSON data-> Python Dict
#     except Exception as e:
#         print(e)
#     print(data)


#     print(request.GET)  # url query params
#     print(request.POST)  # url query params
#     print(request.data) # rest_framework

#     # data['headers'] = request.headers # request.META
#     # print(request.headers)
#     # data['headers'] = json.dumps(dict(request.headers)) # request.META
#     data['headers'] = dict(request.headers) # request.META
#     data['content_type'] = request.content_type
#     data['params'] = request.GET


#     return JsonResponse(data)
###########################################################################
###########################################################################################################################################################
