# Generated by Django 2.1.5 on 2019-02-27 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MorningBriefing', '0006_auto_20190227_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='Link',
            field=models.CharField(max_length=2000, unique=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='Title',
            field=models.CharField(max_length=200),
        ),
    ]
