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




# from django.conf import settings
# import http.client

# import urllib.parse




# def send_otp(mobile ,otp):
#     mobile=str(mobile)
#     otp=str(otp)
#     print("FUNCTION CALLED")
#     conn = http.client.HTTPSConnection("api.msg91.com")
#     authkey = settings.AUTH_KEY 
#     headers = { 'content-type': "application/json" }
#     url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&message="+"Your otp is "+otp +"&mobile="+mobile+"&authkey="+authkey+"&country=880"
#     clean_url = ''.join(char for char in url if ord(char) > 31 and ord(char) < 127)

#      # URL encode
#     clean_url_encoded = urllib.parse.quote(clean_url, safe=':/?&=')  # Encode only necessary characters

#     conn.request("GET", clean_url_encoded , headers=headers)
#     res = conn.getresponse()
#     data = res.read()
#     print(data)
#     print(clean_url_encoded)


#     return None





def generate_otp():
        """Generate a random 4-digit OTP."""
        return random.randint(100000, 999999)




def send_top(mobile_number,email):
    otp =generate_otp()
    user= User.objects.get(mobile_number=mobile_number ,email=email)
    user.otp = otp
    user.save()
    email_id = user.email
    email_subject = "activaton otp!!!"
    email_body = render_to_string('active_email.html', {'otp' : otp})
    email = EmailMultiAlternatives(email_subject , '', to=[email_id])
    email.attach_alternative(email_body, "text/html")
    email.send()
    active_account_url = reverse("active_account") + "?phone_number={}&email={}".format(mobile_number,email)
    clean_url = ''.join(char for char in active_account_url if ord(char) > 31 and ord(char) < 127)
            # URL encode
    clean_url_encoded = urllib.parse.quote(clean_url, safe=':/?&=')  # Encode only necessary characters
    return redirect(active_account_url)




class RegistrationVies(APIView):
    serializer_class = serializers.UserRegistrationSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['mobile_number']
            email = serializer.validated_data['email']
        
            user = User.objects.filter(mobile_number=phone_number).exists()
            if user :return Response("we have a a user with this phone number")
            user = User.objects.filter( email= email).exists()
            if user :return Response("we have a a user with this  email")
            user = serializer.save()
             # Generate OTP
            otp = generate_otp()
            user.otp = otp
            user.save()
           

            active_account_url ="https://food-site-03s7.onrender.com"+ reverse("active_account") + "?phone_number={}&email={}".format(phone_number,email)
            # clean_url = ''.join(char for char in active_account_url if ord(char) > 31 and ord(char) < 127)
            # # URL encode
            # clean_url_encoded = urllib.parse.quote(clean_url, safe=':/?&=')  # Encode only necessary characters
            print(active_account_url)
            try:
                email_id = user.email
                email_subject = "activaton otp!!!"
                email_body = render_to_string('active_email.html', {'otp' : otp})
                email = EmailMultiAlternatives(email_subject , '', to=[email_id])
                email.attach_alternative(email_body, "text/html")
                email.send()
            except Exception as e:
                pass
            
            return Response({"activaton_url":active_account_url ,"status":1})
        return Response(serializer.errors)




class active_account(APIView):
    serializer_class = serializers.TakeOtpSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():

            phone_number = request.query_params.get('phone_number')
            email = request.query_params.get('email')
           # print(unquote("http://127.0.0.1:8000/user_account/active_id/?phone_number=01789534465&emailashikaslam0000%40gmail.com"))
            # email = unquote(email)
            # phone_number = unquote(phone_number)
            #print(email,phone_number)
            user= User.objects.filter(mobile_number=phone_number ,email=email).exists()
            if not user: return Response("no user with this phone number and emil")
            user= User.objects.get(mobile_number=phone_number ,email=email)
            otp1 =  serializer .validated_data['otp']
            otp2 =user.otp
           
            if(otp1==otp2):
                 user.is_active=True
                 user.save()
                 login_url ="http://127.0.0.1:8000"+ reverse("login")
                 return Response({"login_url":login_url,"status":1})
            return Response({"status":0})
        return Response(serializer.errors)
        
           
        
#         
    



class Login_api_view(APIView):
    serializer_class = serializers.loginSerializer
    def post(self,request):
        serializer  = self.serializer_class(data=request.data)
        if  serializer.is_valid():
           
            user_name = serializer .validated_data['user_name']
            password= serializer .validated_data['password']
            phone_number = user_name

            if '@' in user_name or '.com' in user_name:
                user= User.objects.filter(email=user_name).exists()
               # print(user)
                if not user or user == None:return Response({'error' : "Invalid Credential"})
                user= User.objects.get(email=user_name)
                
                phone_number=user.mobile_number
          #  print('the phone is ',phone_number)
            user= User.objects.filter(mobile_number=phone_number).exists()

            if not user or user == None:return Response({'error' : "Invalid Credential"})
            user= User.objects.get(mobile_number=phone_number)
            if user.is_active==False:
                 mobile_number,email = user.mobile_number,user.email
                 send_top(mobile_number,email)
            #print('here')
           # print(user)
            user = authenticate(username=phone_number, password=password)
            #print('get user as ',user)
            if not user or user == None:return Response({'error' : "Invalid Credential"})
           # token, _ = Token.objects.get_or_create(user=user)
            Refresh=RefreshToken.for_user(user)
            login(request,user)
            print(Refresh.access_token)
            return Response({'access_token' :str( Refresh.access_token), 'refress':str( Refresh),'user_id' : user.id,"status":1})
        
             
            
        return Response(serializer.errors)
    



# whey  token, _ = Token.objects.get_or_create(user=user) in this line we have extra _ 

"""
In Python, when unpacking a tuple, you can use the underscore (_) as a placeholder for a value 
you want to discard. In the line >>

The get_or_create method returns a tuple where the first element is the token object and the second element
 is a boolean indicating whether the object was created or not
   (True if created, False if retrieved). However, since you're not interested
     in the second element (whether the object was created or not),
       you can use _ as a placeholder to discard it.

So, the line is essentially saying "get or create a token object for the user, 
and assign the token object to the variable token, ignoring the second element 
returned by get_or_create."





"""
            
            


#return Response({'token' : token.key, 'user_id' : user.id})  
#and here why  token.key why not  token



"""

In Django REST Framework's Token authentication, when you create a 
token for a user, the token is associated with that user and stored 
in the Token model. The key attribute of the token object represents 
the actual token string.

You are returning a dictionary containing the token string 
(token.key) associated with the user and the user's ID. This is 
the typical way to include the token in a response when using
 Token authentication, as it provides the client with the token 
 they need for subsequent authenticated requests.


"""






class Logout_view(APIView):
    
    authentication_classes=[JWTAuthentication]
    def post(self, request):
       # print(request.user.first_name)
        
        print("hello >>  ",request.user.first_name)
        logout(request)
        return Response("successfully logout")
    





class my_profile(APIView):
    authentication_classes=[JWTAuthentication]
    def get(self, request):
       if request.user.is_authenticated:
           user = request.user
           blood_grpup=user.blood_grpup
           gender=user.gender
           email=user.email
           last_name=user.last_name
           first_name=user.first_name
           mobile_number=user.mobile_number
           return Response({
               "blood_grpup":blood_grpup,
           "gender":gender,
           "email":email,
           "last_name":last_name,
           "first_name":first_name,
           "mobile_number":mobile_number,



           })

       return Response("not login user")
    