# Generated by Django 5.0.4 on 2024-04-25 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post_object', '0010_post_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='blood_need_time',
        ),
    ]
