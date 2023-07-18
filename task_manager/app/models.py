from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_creation = models.DateField()
    deadline_date = models.DateField()

    PRIORITY = [(1, 'Высокий'),
                (2, 'Средний'),
                (3, 'Малый')]

    priority_level = models.CharField(max_length=50, choices=PRIORITY, default=1)

    STATUS = [('Не выполнено', 'Не выполнено'), ('Выполнено', 'Выполнено')]

    status = models.CharField(max_length=50, choices=STATUS)

    def __str__(self):
        return f"{self.name} - {self.deadline_date} - {self.priority_level} - {self.status}"

    class Meta:
        ordering = ['deadline_date', 'priority_level']

    def get_absolute_url(self):
        return f"editing/{self.pk}"
