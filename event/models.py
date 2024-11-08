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


class Member(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="members")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name="votes")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="member")
    name = models.CharField(max_length=200)
    state = models.IntegerField(null=False)  # 0: ✕ , 1: △, 2: ◯
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
