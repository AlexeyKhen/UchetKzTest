from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    deadline = models.DateField(null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title
