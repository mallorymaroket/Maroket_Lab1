from django.db import models

class InputName(models.Model):
    name = models.CharField(max_length=20)

class UploadPicture(models.Model):
    picture = models.ImageField(upload_to='image/', verbose_name='Select Profile Picture')

class UpdateInfo(models.Model):
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

class AddItemThisWeek(models.Model):
    key = models.CharField(max_length=5, choices=KEY_TYPES, verbose_name='Key:')
    details = models.CharField(max_length=50, verbose_name='Details:')

class AddItemToday(models.Model):
    key = models.CharField(max_length=5, choices=KEY_TYPES, verbose_name='Key:')
    details = models.CharField(max_length=50, verbose_name='Details:')