# Generated by Django 3.2.3 on 2021-05-21 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routList', '0003_auto_20210521_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rout',
            name='attempts',
            field=models.IntegerField(blank=True),
        ),
    ]
