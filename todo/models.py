from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        pass

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(to=Tag, related_name="tags")

    class Meta:
        ordering = ["-created_at", "is_done"]

    def __str__(self) -> str:
        return self.content
