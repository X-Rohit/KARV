# Generated by Django 4.1 on 2023-03-19 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('coins', models.CharField(max_length=5)),
            ],
        ),
    ]
