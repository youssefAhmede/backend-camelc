# Generated by Django 5.1.2 on 2024-10-23 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='correct',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='school',
            name='timeTaken',
            field=models.FloatField(default=0),
        ),
    ]