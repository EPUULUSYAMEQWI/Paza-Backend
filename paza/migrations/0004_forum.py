# Generated by Django 4.1.2 on 2022-10-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paza', '0003_notification_date_and_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=250, null=True)),
                ('time_date', models.DateTimeField(null=True)),
                ('place', models.CharField(max_length=20)),
                ('moderator', models.CharField(max_length=20)),
            ],
        ),
    ]
