# Generated by Django 5.2.4 on 2025-07-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USERS',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='user', max_length=30)),
                ('mob', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
