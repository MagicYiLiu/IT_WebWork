# Generated by Django 2.1.5 on 2020-03-21 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=20, verbose_name='UserName')),
                ('UserPasswd', models.CharField(max_length=20, verbose_name='UserPasswd')),
                ('UserAge', models.CharField(max_length=30, verbose_name='UserAge')),
            ],
        ),
    ]
