# Generated by Django 5.0.6 on 2024-06-03 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='completed',
            field=models.BooleanField(null=True),
        ),
    ]
