# Generated by Django 5.0.4 on 2024-04-25 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_object', '0009_remove_post_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
