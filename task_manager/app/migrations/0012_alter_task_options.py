# Generated by Django 4.2.3 on 2023-07-18 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['deadline_date', '-priority_level']},
        ),
    ]
