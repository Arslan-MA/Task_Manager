# Generated by Django 4.2.3 on 2023-07-18 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-priority_level', 'deadline_date']},
        ),
    ]
