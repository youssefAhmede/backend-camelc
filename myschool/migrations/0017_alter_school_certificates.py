# Generated by Django 5.1.2 on 2024-10-27 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0016_alter_school_certificates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='certificates',
            field=models.JSONField(default=list),
        ),
    ]
