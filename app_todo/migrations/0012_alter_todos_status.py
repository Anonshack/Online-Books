# Generated by Django 4.2.4 on 2023-11-10 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0011_alter_todos_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.CharField(choices=[('d', 'done'), ('a', 'active'), ('n', 'not yet')], max_length=15, verbose_name='Status'),
        ),
    ]
