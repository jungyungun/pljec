# Generated by Django 2.1.5 on 2019-02-18 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MorningBriefing', '0004_auto_20190217_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Usage',
        ),
    ]
