# Generated by Django 5.1.2 on 2024-10-27 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0018_alter_school_certificates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='certificates',
            field=models.JSONField(default=[{'date': '', 'name': ''}, {'date': '', 'name': ''}]),
        ),
    ]