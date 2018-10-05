# Generated by Django 2.1.2 on 2018-10-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.CharField(max_length=5)),
                ('temp_min', models.CharField(max_length=5)),
                ('temp_max', models.CharField(max_length=5)),
                ('pressure', models.IntegerField()),
                ('humidity', models.CharField(max_length=5)),
                ('last_update', models.DateTimeField()),
            ],
        ),
    ]