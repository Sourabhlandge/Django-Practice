# Generated by Django 3.1.5 on 2021-02-11 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=264)),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=264)),
                ('subject', models.CharField(max_length=64)),
                ('salary', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
