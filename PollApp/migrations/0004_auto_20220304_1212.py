# Generated by Django 3.1.14 on 2022-03-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PollApp', '0003_auto_20220304_0952'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('poll', 'user')},
        ),
    ]
