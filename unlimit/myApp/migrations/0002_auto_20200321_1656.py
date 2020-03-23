# Generated by Django 2.1.5 on 2020-03-21 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DateField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'User data',
            },
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='userdata',
            name='users',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
