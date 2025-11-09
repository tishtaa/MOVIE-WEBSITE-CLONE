from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal')
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    profiles=models.ManyToManyField('Profile')


class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    image=models.ImageField(upload_to='profiles',blank=True,null=True)


    def __str__(self):
        return self.name +" "+self.age_limit

class Movie(models.Model):
    title=models.CharField(max_length=225)
    description=models.TextField(blank=True, null=True)
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    videos=models.ManyToManyField('Video')
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True)
    background=models.ImageField(upload_to='backgrounds',blank=True,null=True)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)
    is_showcase=models.BooleanField(default=False)

class Video(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    
    

    

