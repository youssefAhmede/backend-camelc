# Generated by Django 5.1.2 on 2024-10-23 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myschool', '0003_school_correctq2_school_timeq2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='correct',
            new_name='correctQ1',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='timeTaken',
            new_name='timeQ1',
        ),
        migrations.RemoveField(
            model_name='school',
            name='name',
        ),
    ]
