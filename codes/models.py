from django.db import models
from django.contrib.auth.models import User


class CodesUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=32, blank=True)
    education = models.CharField(max_length=255, blank=True)
    experience = models.CharField(max_length=255, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    position = models.CharField(max_length=255, blank=True)
    specification = models.CharField(max_length=255, blank=True)
    interests = models.CharField(max_length=255, blank=True)
    telegram = models.CharField(max_length=255, blank=True)
    profile_pic = models.ImageField(blank=True)


##
# email
# first name
# last name
#
#!!!!!! "uid": this.createUserId(),
## "name1": s.firstName,
## "name2": s.secondName,
## "name3": s.thirdName,
## "phone": s.phone,
## "experience": s.experience,
## "position": s.position,
## "education": s.education,
## "organization": s.organization,
## "specification": s.specification,
## "interests": s.interests,
####### "telegram": s.telegram,
# "pic": e.data._id,
#!!!!! "owner": createUserQuery.data.id,

class Meeting(models.Model):
    title = models.CharField(max_length=255, blank=True)
    preview_desc = models.TextField(blank=True)
    timestamp = models.DateTimeField(blank=True)
    city = models.CharField(max_length=255, blank=True)
    lat = models.FloatField(blank=True)
    lng = models.FloatField(blank=True)
    preview_img = models.ImageField(blank=True)
    main_img = models.ImageField(blank=True)
    full_desc = models.TextField(blank=True)
