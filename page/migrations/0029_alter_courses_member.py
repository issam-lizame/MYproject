# Generated by Django 4.1.7 on 2023-03-16 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0028_remove_members_cours_courses_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='page.members'),
        ),
    ]
