# Generated by Django 4.2.3 on 2023-07-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_task_priority_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority_level',
            field=models.CharField(choices=[('Высокий', 'Высокий'), ('Средний', 'Средний'), ('Малый', 'Малый')], max_length=50),
        ),
    ]
