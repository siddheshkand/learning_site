from django.db import models


# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    order = models.IntegerField(default=0, unique=True)
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ['order', ]

    def __str__(self):
        return self.title
