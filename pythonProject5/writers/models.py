from django.db import models


class Articles(models.Model):
    title=models.CharField(max_length=254)
    post=models.TextField()
    date=models.DateTimeField()
    def __str__(self):
        return self.title
