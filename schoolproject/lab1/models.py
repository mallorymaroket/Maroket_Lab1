from django.db import models

class UpdateProfile(models.Model):
    picture = models.ImageField(upload_to='image/', verbose_name='Select Profile Picture')