# Generated by Django 4.0.1 on 2022-01-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image1',
            field=models.ImageField(default='default.jpeg', upload_to='property_images/'),
        ),
        migrations.AddField(
            model_name='property',
            name='image2',
            field=models.ImageField(default='default.jpeg', upload_to='property_images/'),
        ),
        migrations.AddField(
            model_name='property',
            name='image3',
            field=models.ImageField(default='default.jpeg', upload_to='property_images/'),
        ),
    ]
