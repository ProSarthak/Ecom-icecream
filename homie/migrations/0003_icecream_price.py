# Generated by Django 4.0.5 on 2022-07-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homie', '0002_icecream'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='price',
            field=models.IntegerField(default=499),
        ),
    ]
