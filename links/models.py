from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return str(self.link)


class LinkDetail(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE)
    section = models.TextField()

    lazy = models.IntegerField(default=0)

    def __str__(self):
        return str(self.link)
