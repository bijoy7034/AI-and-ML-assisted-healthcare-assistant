# Generated by Django 3.2 on 2024-03-07 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_ment_my_time_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='ment',
            name='Disease',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='ment',
            name='Doctor_Name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]