from django.db import models


class Link(models.Model):
    link = models.CharField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.link}"


class LinkDetail(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE)
    section = models.TextField()

    # if a link doesn't change after 50 check, lazy will be true
    # next time it won't check for changes
    # will check again after 2 hours
    lazy = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.link.id} -  {self.link}"
