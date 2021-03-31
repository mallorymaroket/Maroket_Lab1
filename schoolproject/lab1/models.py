from django.db import models

class UploadProfile(models.Model):
    picture = models.ImageField(upload_to='media/', verbose_name='Select Profile Picture')