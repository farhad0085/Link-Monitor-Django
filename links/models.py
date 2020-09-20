from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.link}"


class LinkDetail(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE)
    section = models.TextField()

    def __str__(self):
        return f"{self.link.id} -  {self.link}"
