# Generated by Django 4.1.7 on 2023-03-15 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='Gender',
            field=models.CharField(default='Male', max_length=10),
        ),
    ]
