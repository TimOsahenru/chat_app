from django.db import models


class Post(models.Model):
    body = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
