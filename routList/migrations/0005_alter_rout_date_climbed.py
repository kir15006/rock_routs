# Generated by Django 3.2.3 on 2021-05-21 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routList', '0004_alter_rout_attempts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rout',
            name='date_climbed',
            field=models.DateField(blank=True, null=True),
        ),
    ]