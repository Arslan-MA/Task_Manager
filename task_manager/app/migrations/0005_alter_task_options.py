# Generated by Django 4.2.3 on 2023-07-18 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_task_priority_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-deadline_date', 'priority_level']},
        ),
    ]
