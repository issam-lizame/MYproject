# Generated by Django 4.1.7 on 2023-03-15 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_members_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Gob',
            field=models.TextField(blank=True),
        ),
    ]
