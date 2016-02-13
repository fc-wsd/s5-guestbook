from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=40, null=False)
    content = models.TextField(null=False, max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}번 글'.format(self.pk)

