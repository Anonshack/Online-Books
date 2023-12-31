# Generated by Django 4.2.4 on 2023-10-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0004_alter_todos_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.CharField(choices=[('n', 'not yet'), ('a', 'active'), ('d', 'done')], max_length=15, verbose_name='Status'),
        ),
    ]
