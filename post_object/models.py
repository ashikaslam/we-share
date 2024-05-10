from django.db import models

from user_account.models import User
# Create your models here.

BLOOD_CHOICES = [
    ('A+', 'A+'),
    ('B+', 'B+'),
    ('AB+', 'AB+'),
    ('O+', 'O+'),
   ('A-', 'A-'),
    ('B-', 'B-'),
    ('AB-', 'AB-'),
    ('O-', 'O-'),
]


RATING_CHOICES = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
]






class Post(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE,related_name="my_post",blank=True,default=None,null=True)
    title=models.CharField( max_length=250)
    description=models.TextField()
    image1=models.ImageField(upload_to='photos/post',blank=True,null=True,default=None)
    phone_number = models.CharField(max_length=13,blank=True,null=True,default=None)
    blood_grpup=models.CharField(choices =BLOOD_CHOICES,max_length=3)
    amount = models.IntegerField(default=1)
    post_time=models.DateTimeField(auto_now=False, auto_now_add=True)
    post_update_time=models.DateTimeField(auto_now=True, auto_now_add=False)
    blood_need_time= models.DateTimeField(auto_now=False, auto_now_add=False,blank=True,null=True,default=None)
    apply_availavle=models.BooleanField(default=True)
    people_apply=models.IntegerField(default=0)
    at_leas_5_people_managed=models.IntegerField(default=0)
    donate_done=models.BooleanField(default=False)
    helper=models.ManyToManyField(User,  related_name="i_helped",blank=True,default=None,null=True)


    # address

    country = models.CharField(max_length=50, blank=False)
    district = models.CharField(max_length=50, blank=False)
    upazila = models.CharField(max_length=50, blank=False)
    unionOrtown = models.CharField(max_length=50, blank=False)
    villageOrrad = models.CharField(max_length=50, blank=False)
    zip_code = models.CharField(max_length=5)
    hospital_name=models.CharField( max_length=50)

    class Meta:
       # ordering = ['-post_time']  # Sort by post_time in descending order
       pass





class Coments(models.Model):
     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='coments',blank=True,null=True)
     user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
     discription = models.TextField()
     created_at = models.DateTimeField(auto_now_add = True)

    




    