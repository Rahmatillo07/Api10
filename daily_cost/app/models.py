from django.db import models
from django.contrib.auth.models import User


class Cost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    amount = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return self.title