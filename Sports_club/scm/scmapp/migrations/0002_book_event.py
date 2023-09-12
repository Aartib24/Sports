# Generated by Django 4.2.4 on 2023-08-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_event',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('mobile', models.IntegerField(max_length=10)),
            ],
        ),
    ]
