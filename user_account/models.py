from django.db import models

# Create your models here.



from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, mobile_number, password,first_name,last_name,email ):
        if not mobile_number:
            raise ValueError("Mobile number is required.")
        if not password:
            raise ValueError("password is required.")
        
        if not first_name:
            raise ValueError("first_name is required.")
        
        if not last_name:
            raise ValueError("last_name is required.")
        if not email:
            raise ValueError("email is required.")
        # if not birth_day:
        #     raise ValueError("birth_day is required.")
        
        user = self.model(mobile_number=mobile_number,
                           username=mobile_number,
                           first_name=first_name,
                           last_name=last_name,
                           email=email,
                          # birth_day=birth_day
                           )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password,first_name,last_name,email):
        user = self.create_user(mobile_number, password, first_name,last_name,email)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


STAR_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]


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

GENDER_CHOICES = [
    ('male', 'male'),
    ('female', 'female'),
   
]
RATING_CHOICES = [
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
]


class User(AbstractUser):
    mobile_number = models.CharField(max_length=13, null=False, unique=True)
    otp = models.CharField(max_length=6,blank=True)
    first_name=models.CharField( max_length=50, blank=False)
    last_name=models.CharField( max_length=50, blank=False)
    email =models.CharField(max_length=100,blank=False)
   # birth_day=models.DateField(auto_now=False, auto_now_add=False)
    gender=models.CharField(max_length=10,choices =GENDER_CHOICES,null=True,default=None)
    blood_grpup=models.CharField(choices =BLOOD_CHOICES,max_length=3)
    USERNAME_FIELD = "mobile_number"
    REQUIRED_FIELDS = ['first_name','last_name','email']
    objects = UserManager()






class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='porfile')
    profile_pic =models.ImageField(upload_to='photos/user_profile',blank=True)
    total_donate = models.IntegerField(default=0)
    tata_amount_of_blood=models.DecimalField(max_digits=5, decimal_places=2,default=0.0)
    rating = models.DecimalField(max_digits=3, decimal_places=1,default=0.0,choices=RATING_CHOICES)
    




class Adrress(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='address')
    country = models.CharField(max_length=50, blank=False)
    district = models.CharField(max_length=50, blank=False)
    upazila = models.CharField(max_length=50, blank=False)
    unionOrtown = models.CharField(max_length=50, blank=False)
    villageOrrad = models.CharField(max_length=50, blank=False)
    zip_code = models.CharField(max_length=5)
    


