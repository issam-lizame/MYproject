# Generated by Django 4.1.7 on 2023-03-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_alter_members_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='Email',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='lastName',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='members',
            name='password',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
