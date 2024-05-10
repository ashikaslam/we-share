





from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

#router.register('Patient', views.PatientViewSet)

##router.register('ragistartion', views.UserRegistrationApiView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
   # path('', include(router.urls)),

  path('post/',views.create_post.as_view(),name='post'),
  path('home/',views.RecentPost.as_view(),name='home'),
  path('coment/',views.create_coment.as_view(),name='coment'),
  path('get_coment_for_a_post/',views.get_coment_for_a_post.as_view(),name='get_coment_for_a_post'),
   
    
]
