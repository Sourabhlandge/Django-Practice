# Generated by Django 3.1.5 on 2021-02-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProxyEmployee',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('cm_app.employee',),
        ),
        migrations.CreateModel(
            name='ProxyEmployee2',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('cm_app.employee',),
        ),
    ]
