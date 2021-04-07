# Generated by Django 3.1.7 on 2021-04-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab1', '0003_auto_20210407_0533'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, verbose_name='Update Nickname:')),
                ('bio', models.TextField(verbose_name='Update Bio:')),
            ],
        ),
        migrations.CreateModel(
            name='UploadPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='image/', verbose_name='Select Profile Picture')),
            ],
        ),
        migrations.DeleteModel(
            name='UpdateProfile',
        ),
    ]
