# Generated by Django 3.1.3 on 2020-11-10 04:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('userid', models.CharField(max_length=18)),
                ('regdate', models.DateTimeField(default=django.utils.timezone.localtime)),
                ('views', models.IntegerField(default=0)),
                ('contents', models.TextField()),
                ('thumbup', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('hdate', models.DateField()),
                ('jobid', models.CharField(max_length=255)),
                ('sal', models.IntegerField()),
                ('comm', models.FloatField()),
                ('mgrid', models.IntegerField()),
                ('deptid', models.IntegerField()),
            ],
        ),
    ]
