# Generated by Django 4.2.4 on 2023-10-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0003_savoljavob'),
    ]

    operations = [
        migrations.AddField(
            model_name='savoljavob',
            name='is_superadmin',
            field=models.BooleanField(default=False),
        ),
    ]
