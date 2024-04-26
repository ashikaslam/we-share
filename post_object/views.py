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

class create_post(APIView):
    serializer_class = serializers.PostSerializer
    authentication_classes=[JWTAuthentication]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        if request.user.is_authenticated:
            # Extract image file from request.FILES
            image_file = request.FILES.get('image1')
            # Remove 'impage1' key from request.data to avoid conflict with serializer
            request.data.pop('image1', None)
            # Pass image_file to serializer as context
            serializer = self.serializer_class(data=request.data, context={'image_file': image_file})
            if serializer.is_valid():
                try:
                    the_post = serializer.save()
                    # Update the_post with user before saving
                    the_post.user = request.user
                    the_post.image1=image_file
                    the_post.save()
                    if not the_post.user:
                        the_post.delete()
                        return Response({'status': 0})
                    return Response({'status': 1})
                except Exception as e:
                    return Response({'status': 0})
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
     





            
               



