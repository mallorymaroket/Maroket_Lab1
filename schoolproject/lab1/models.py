from django.db import models

class UploadProfile(models.Model):
    picture = models.ImageField(upload_to='images', verbose_name='Select Profile Picture')

""" class EditInfo(models.Model):
    nickname = RichTextField
    bio """