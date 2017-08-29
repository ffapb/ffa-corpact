from django.db import models

# Create your models here.
class Event(models.Model):
    start_datetime = models.DateTimeField()
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
      return self.title

    def get_absolute_url(self):
      return "bla"
