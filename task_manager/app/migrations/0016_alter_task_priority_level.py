# Generated by Django 4.2.3 on 2023-07-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_task_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority_level',
            field=models.CharField(choices=[(1, 'Высокий'), (2, 'Средний'), (3, 'Малый')], max_length=50),
        ),
    ]
