from django.db import models

class InputName(models.Model):
    name = models.CharField(max_length=20)

class UpdateProfile(models.Model):
    picture = models.ImageField(upload_to='image/', verbose_name='Select Profile Picture')
    nickname = models.CharField(max_length=20, verbose_name='Update Nickname:')
    bio = models.TextField(verbose_name='Update Bio:')

KEY_TYPES=[
        ('Task','Task'),
        ('Event','Event'),
        ('Note','Note'),
    ]

class AddKey(models.Model):
    key = models.CharField(max_length=5,choices=KEY_TYPES, verbose_name='Key:')
    description = models.CharField(max_length=50, verbose_name='Description:')

class AddItem(models.Model):
    key = models.CharField(max_length=5, choices=KEY_TYPES, verbose_name='Key:')
    details = models.CharField(max_length=50, verbose_name='Details:')