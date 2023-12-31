# Generated by Django 4.2.5 on 2023-10-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.CharField(choices=[('d', 'done'), ('n', 'not yet'), ('a', 'active')], max_length=15, verbose_name='Status'),
        ),
    ]