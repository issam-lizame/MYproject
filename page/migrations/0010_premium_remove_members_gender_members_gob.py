# Generated by Django 4.1.7 on 2023-03-16 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_delete_premium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='members',
            name='Gender',
        ),
        migrations.AddField(
            model_name='members',
            name='Gob',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
