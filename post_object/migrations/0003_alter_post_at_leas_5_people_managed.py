# Generated by Django 5.0.4 on 2024-04-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post_object', '0002_alter_post_people_apply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='at_leas_5_people_managed',
            field=models.IntegerField(default=0),
        ),
    ]
