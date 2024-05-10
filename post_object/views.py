from django.shortcuts import render
from .import serializers
# Create your views here.
from django.shortcuts import redirect
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from django.urls import reverse

import urllib.parse



from .models import User  # Import the User model
from . import serializers 


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.contrib.auth import authenticate, login,logout

from urllib.parse import unquote

from rest_framework.authtoken.models import Token
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from. import models
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

class create_post(APIView):
    serializer_class = serializers.PostSerializer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        if request.user.is_authenticated:
            # Extract image file from request.FILES
            image_file = request.FILES.get('image1')
            # Remove 'impage1' key from request.data to avoid conflict with serializer
            request.data.pop('image1', None)
            # # Pass image_file to serializer as context
            serializer = self.serializer_class(data=request.data )
            #serializer = self.serializer_class(data=request.data '''context={'image_file': image_file}''')
            if serializer.is_valid():
                    print("yes valied>>>>")
               # try:
                    the_post = serializer.save()
                    # Update the_post with user before saving
                    the_post.user = request.user
                    the_post.image1=image_file
                    the_post.save()
                    if not the_post.user:
                        the_post.delete()
                        return Response({'status': 0})
                    return Response({'status': 1})
                # except Exception as e:
                #     return Response({'status': 0})
            else:
                return Response(serializer.errors)
        else:
            return Response({'status': 0})








class RecentPost(APIView):
     def get(self, request):
          
          id_value = request.GET.get('id')
          print("the id is  >>>>", id_value)
          if id_value:
              id_value=int(id_value)
              post = models.Post.objects.filter(id=id_value).exists()
              if post:
                   post = models.Post.objects.filter(id=id_value).values()
                   return JsonResponse({'post': list(post)})
              else :return JsonResponse({'error': "post not found"})


          all_post = models.Post.objects.filter(apply_availavle=True).values()
          return JsonResponse({'all_post': list(all_post)})
     





            
               


class create_coment(APIView):
    serializer_class = serializers.ComentsSerializer
    authentication_classes=[JWTAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        print('inside the coment1')
        if request.user.is_authenticated :
             print('inside the coment2')
             serializer = self.serializer_class(data=request.data )
             if serializer.is_valid():
                  id_value = request.GET.get('id')
                  print(id_value)
                  if id_value:
                    id_value=int(id_value)
                    our_post = models.Post.objects.filter(id=id_value).exists()
                    if our_post:
                     print('yes we have post')
                     our_post = models.Post.objects.get(id=id_value)
                     coment = serializer.save()
                     coment.user=request.user
                     coment.post=our_post
                     print("the user is ", request.user)
                     print(our_post)

                     coment.save()
                     return Response("done")


                  
             else :
                 print("not valied")
                 return Response(serializer.errors)
        return Response("error")
            
             

def fun(coment):
    dic ={
    "user_id":coment.user.id,
    "post_id":coment.post.id,
    "user_name":f"""{coment.user.first_name}  {coment.user.last_name}""",
    "coment_text":coment.discription,
    "time":coment.created_at,

    }
    return dic





class get_coment_for_a_post(APIView):
    def get(self, request):
                  id_value = request.GET.get('id')
                  print(id_value)
                  if id_value:
                    id_value=int(id_value)
                    our_post = models.Post.objects.filter(id=id_value).exists()
                    if our_post:
                     print('yes we have post')
                     our_post = models.Post.objects.get(id=id_value) 
                     all_the_coment = our_post.coments.all()
                     arr = []
                     for i in  all_the_coment:
                         now = fun(i)
                         arr.append(now)

                     return JsonResponse({'all_the_coment': list(arr)})
                     
