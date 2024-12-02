# Generated by Django 5.1.2 on 2024-10-30 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0022_remove_school_profile_link_alter_school_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]