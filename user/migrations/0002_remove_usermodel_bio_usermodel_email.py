# Generated by Django 4.0.1 on 2022-01-31 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='bio',
        ),
        migrations.AddField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=256),
        ),
    ]
