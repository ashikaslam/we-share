
from.models import User
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
     confirm_password = serializers.CharField(required = True)
     class Meta:
        model =  User
        fields = ['user','first_name','last_name','email',"mobile_number",'password', 'confirm_password','gender','blood_grpup']
    

     def save(self):
        mobile_number = self.validated_data['mobile_number']
        password = self.validated_data['password']
        first_name= self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password2 = self.validated_data['confirm_password']
       # birth_day = self.validated_data['birth_day']
        gender = self.validated_data['gender']
        blood_grpup = self.validated_data['blood_grpup']
       # print("birtday is ",birth_day)
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
        

        account = User(mobile_number=mobile_number,username=mobile_number,
                        first_name=first_name,
                           last_name=last_name,
                           email=email,
                          #birth_day=birth_day,
                          blood_grpup=blood_grpup,
                           gender= gender
                       
                       )
        account.set_password(password)
        account.is_active = False
        account.save()
        return account













# from.models import User
# from rest_framework import serializers

# class UserLoginSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required=True)

#     class Meta:
#         model = User
#         fields = ["mobile_number", "password", "confirm_password"]

#     def validate(self, attrs):
#         if attrs["password"] != attrs["confirm_password"]:
#             raise serializers.ValidationError({"error": "Passwords don't match"})
#         return attrs

#     def save(self, validated_data):
      #   mobile_number = validated_data["mobile_number"]
      #   password = validated_data["password"]

      #   # Call create_user method of custom UserManager
      #   user = User.objects.create_user(mobile_number=mobile_number, password=password)
      #   user.is_active = False
      #   user.save()

      #   return user





class TakeOtpSerializer(serializers.Serializer):
    otp = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter the  OTP we sent in your email'})


class loginSerializer(serializers.Serializer):
    user_name = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your Phone or email'})
    password = serializers.CharField(required=True, allow_blank=False,  style={'placeholder': 'Enter your password'})
   