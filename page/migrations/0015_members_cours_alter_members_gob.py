# Generated by Django 4.1.7 on 2023-03-16 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_alter_members_gob'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='cours',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='page.courses'),
        ),
        migrations.AlterField(
            model_name='members',
            name='Gob',
            field=models.CharField(blank=True, default='Develppeur', max_length=20, null=True),
        ),
    ]
