from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    completed = models.BooleanField(default=False, blank=True, null=True, verbose_name="Completed")
    token = models.CharField(max_length=200, blank=True, null=True, verbose_name="Token")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Updated at")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        db_table = "tasks"
        ordering = ["-created_at"]
