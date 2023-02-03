from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Task(models.Model):
    """ Task of todo list """
    URGENCY_LEVEL_0 = '0'
    URGENCY_LEVEL_1 = '1'
    URGENCY_LEVEL_2 = '2'

    URGENCY_CHOICES = [
        (URGENCY_LEVEL_0, 'Normal'),
        (URGENCY_LEVEL_1, 'Important'),
        (URGENCY_LEVEL_2, 'Very important'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    urgency = models.CharField(max_length=63,
                               choices=URGENCY_CHOICES,
                               default=URGENCY_LEVEL_0)
    tags = models.ManyToManyField(Tag)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Task: {self.name}, completed: {self.completed}'

    class Meta:
        ordering = ['updated_at']
