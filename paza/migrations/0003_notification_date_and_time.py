# Generated by Django 4.1.2 on 2022-10-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paza', '0002_remove_notification_date_and_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date_and_time',
            field=models.DateTimeField(null=True),
        ),
    ]
