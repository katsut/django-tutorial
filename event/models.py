from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Choice(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="choices")
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.date
