# Generated by Django 4.0.1 on 2022-01-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0002_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='cost',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
