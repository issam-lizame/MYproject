# Generated by Django 4.1.7 on 2023-03-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0024_rename_section_members_cours_remove_members_id1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='date_join',
            field=models.DateField(),
        ),
    ]
