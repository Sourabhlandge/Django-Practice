# Generated by Django 2.2.3 on 2020-12-25 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='marks',
            field=models.IntegerField(),
        ),
    ]
