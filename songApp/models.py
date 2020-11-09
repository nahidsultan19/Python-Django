from django.db import models


class Band(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Songs(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
