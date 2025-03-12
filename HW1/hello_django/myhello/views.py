

# # Create your views here.
# #from django.http import HttpResponse

# def myIndex(request):
#     my_name = request.GET.get('name', "CGU")
#     return HttpResponse("Hello " + my_name)

#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.serializers.json import DjangoJSONEncoder
import json
import logging

# class HelloApiView(APIView):
#     def get(self, request):
#         my_name = request.GET.get('name' , None)
#         if my_name:
#             retValue = {}
#             retValue['data'] = "Hello" + my_name
#             return Response(retValue, status=status.HTTP_200_OK)
#         else:
#             return Response(
#                 {"res": "parameter: name is None"},
#                 status=status.HTTP_400_BAD_REQUEST
#             )

# from .models import Post
# from .models import User
logger = logging.getLogger('django')

# @api_view(['GET'])
# def add_post(request):
#     title = request.GET.get('title' , '')
#     content = request.GET.get('content' , '')
#     photo = request.GET.get('photo' , '')
#     location = request.GET.get('location' , '')
    
#     new_post = Post()
#     new_post.title = title
#     new_post.content = content
#     new_post.photo = photo
#     new_post.location = location
#     new_post.save()
#     logger.debug(" *** myhello_api: " + title)
#     if title:
#         return Response({"data": title + " insert!"}, status=status.HTTP_200_OK)
#     else:
#         return Response(
#             {"res": "parameter: name is None"},
#             status = status.HTTP_400_BAD_REQUEST
#         )

# @api_view(['GET'])
# def list_post(request):
#     posts = Post.objects.all().values()
#     return JsonResponse(list(posts), safe=False)
    # return Response({"data":
    #             json.dumps(
    #                list(posts),
    #                 sort_keys = True,
    #                 indent = 1,
    #                 cls = DjangoJSONEncoder)},
    #             status = status.HTTP_200_OK)
    
# @api_view(['GET'])
# def list_users(request):
#     users = User.objects.all().values()
#     return JsonResponse(list(users), safe=False)
#     # return Response({"data":
#     #             json.dumps(
#     #                list(posts),
#     #                 sort_keys = True,
#     #                 indent = 1,
#     #                 cls = DjangoJSONEncoder)},
#     #             status = status.HTTP_200_OK)

from .models import Post

@api_view(['GET'])
def addcourse_post(request):
    開課單位 = request.GET.get('開課單位' , '')
    開課名稱 = request.GET.get('開課名稱' , '')
    授課教師 = request.GET.get('授課教師' , '')
    
    new_post = Post()
    new_post.開課單位 = 開課單位
    new_post.開課名稱 = 開課名稱
    new_post.授課教師 = 授課教師
    new_post.save()
    logger.debug(" *** myhello_api: " + 開課單位)
    if 開課單位:
        return Response({"data": 開課單位 + " insert!"}, status=status.HTTP_200_OK)
    else:
        return Response(
            {"res": "parameter: name is None"},
            status = status.HTTP_400_BAD_REQUEST
        )
        
@api_view(['GET'])
def courselist_post(request):
    posts = Post.objects.all().values()
    return JsonResponse(list(posts), safe=False)