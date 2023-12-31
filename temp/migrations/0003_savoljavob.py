# Generated by Django 4.2.4 on 2023-10-08 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_javob'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavolJavob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('javoblar', models.ManyToManyField(related_name='savoljavob_set', to='temp.javob')),
                ('savol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='javoblar', to='temp.javob')),
            ],
        ),
    ]
