# Generated by Django 5.2.4 on 2025-08-01 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prac_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
