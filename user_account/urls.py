from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

#router.register('Patient', views.PatientViewSet)

##router.register('ragistartion', views.UserRegistrationApiView)

# The API URLs are now determined automatically by the router.
urlpatterns = [
   # path('', include(router.urls)),

   path('register/',views.RegistrationVies.as_view(),name='register'),
   path('login/',views.Login_api_view.as_view(),name='login'),
   path('active_id/',views.active_account.as_view(),name='active_account'),
   path('my_profile/',views.my_profile.as_view(),name='my_profile'),
    
]
