# Generated by Django 4.2.5 on 2023-10-06 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Todo title')),
                ('description', models.TextField(verbose_name='Full text todo')),
                ('start_time', models.DateField(verbose_name='Start time')),
                ('end_time', models.DateField(verbose_name='End time')),
                ('status', models.CharField(choices=[('n', 'not yet'), ('a', 'active'), ('d', 'done')], max_length=15, verbose_name='Status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'db_table': 'todo_list',
                'ordering': ['start_time', 'title'],
            },
        ),
    ]