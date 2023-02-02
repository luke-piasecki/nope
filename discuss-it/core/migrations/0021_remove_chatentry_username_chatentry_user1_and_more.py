# Generated by Django 4.1.4 on 2023-01-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_alter_chatentry_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatentry',
            name='username',
        ),
        migrations.AddField(
            model_name='chatentry',
            name='user1',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='chatentry',
            name='user2',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='people',
            name='reports',
            field=models.IntegerField(default=0),
        ),
    ]
