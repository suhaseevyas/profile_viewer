# Generated by Django 3.0.6 on 2020-07-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_regi_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regi',
            name='email',
            field=models.CharField(max_length=30),
        ),
    ]
