# Generated by Django 5.1.6 on 2025-02-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_cuisinetype_delete_cuisine_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuisinetype',
            name='description',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
