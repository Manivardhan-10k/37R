# Generated by Django 5.2.4 on 2025-07-30 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('env_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
