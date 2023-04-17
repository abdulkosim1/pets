# Generated by Django 4.1.6 on 2023-04-17 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_post', '0002_pets_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='pets',
            name='age',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='pets',
            name='contact',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='pets',
            name='pet_name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
