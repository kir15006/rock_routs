# Generated by Django 3.2.3 on 2021-05-21 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routList', '0005_alter_rout_date_climbed'),
    ]

    operations = [
        migrations.AddField(
            model_name='rout',
            name='notes',
            field=models.TextField(default='No notes'),
        ),
    ]