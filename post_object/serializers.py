
from.models import User
from rest_framework import serializers
from .models import Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'image1','description', 'phone_number', 'blood_grpup', 'amount', 'blood_need_time', 'country', 'district', 'upazila', 'unionOrtown', 'villageOrrad', 'zip_code', 'hospital_name']
            
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