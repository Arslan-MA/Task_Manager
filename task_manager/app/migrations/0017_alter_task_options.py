# Generated by Django 4.2.3 on 2023-07-18 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_task_priority_level'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['priority_level', 'deadline_date']},
        ),
    ]
