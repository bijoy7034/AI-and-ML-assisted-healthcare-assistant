# Generated by Django 3.2 on 2024-03-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_ment_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='ment',
            name='my_time_field',
            field=models.TimeField(null=True),
        ),
    ]
