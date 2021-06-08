from django.db import models
from helpers.models import TrackingModel
from authentication.models import User
from categories.models import Category


class Template(TrackingModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title