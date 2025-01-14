from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey("auth.User", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
