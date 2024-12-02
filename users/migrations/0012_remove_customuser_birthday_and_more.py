# Generated by Django 5.1.2 on 2024-11-29 18:26

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_customuser_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=150, verbose_name='last name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='', error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]
