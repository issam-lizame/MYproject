# Generated by Django 4.1.7 on 2023-03-16 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0027_alter_members_date_join'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='cours',
        ),
        migrations.AddField(
            model_name='courses',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='page.members'),
        ),
    ]
