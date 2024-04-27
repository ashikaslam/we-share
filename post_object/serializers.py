
from.models import User
from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image1','description', 'phone_number', 'blood_grpup', 
                  'amount', 'blood_need_time', 'country', 'district', 'upazila', 'unionOrtown', 'villageOrrad', 
                  'zip_code', 'hospital_name']
            




    def save(self):
        title = self.validated_data['title']
        description = self.validated_data['description']
       # phone_number= self.validated_data['phone_number']
        blood_grpup = self.validated_data['blood_grpup']
        amount = self.validated_data['amount']
        blood_need_time = self.validated_data['blood_need_time']
       # birth_day = self.validated_data['birth_day']
        country = self.validated_data['country']
        district = self.validated_data['district']
        villageOrrad = self.validated_data['villageOrrad']
        unionOrtown = self.validated_data['unionOrtown']
        upazila = self.validated_data['upazila']
        hospital_name = self.validated_data['hospital_name']
        zip_code = self.validated_data['zip_code']
       # print("birtday is ",birth_day)
        
        post = Post(
              
        title = title,
        description = description,
       # phone_number= phone_number,
        blood_grpup = blood_grpup,
        amount = amount,
        blood_need_time =blood_need_time,
       # birth_day = self.validated_data['birth_day']
        country = country,
        district = district,
        villageOrrad = villageOrrad,
        unionOrtown = unionOrtown,
        upazila = upazila,
        hospital_name = hospital_name,
        zip_code = zip_code



                       
                       )
        
        
        
        return post
    # def create(self, validated_data):
    #     # Access image file from context
    #     image_file = self.context.get('image_file')
    #     # Set 'impage1' field with the uploaded file
    #     validated_data['impage1'] = image_file
    #     return super().create(validated_data)




    # def save(self, **kwargs):
    #     post_data = self.validated_data
    #     post = Post.objects.create(**post_data)
    #     return post
    # i cna go with this code or without  'blood_need_time',