# Generated by Django 4.2.1 on 2023-05-31 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('email', models.CharField(unique=True)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
