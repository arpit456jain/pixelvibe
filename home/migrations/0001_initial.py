# Generated by Django 3.2.6 on 2021-09-14 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('content', models.TextField(max_length=400)),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Arts')),
            ],
        ),
    ]
