from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=40)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{date} 만들어진 {number}번 글'.format(
            date=self.created_at, number=self.pk
        )
