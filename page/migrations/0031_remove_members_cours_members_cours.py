# Generated by Django 4.1.7 on 2023-03-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0030_remove_courses_member_members_cours'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='cours',
        ),
        migrations.AddField(
            model_name='members',
            name='cours',
            field=models.ManyToManyField(to='page.courses'),
        ),
    ]
