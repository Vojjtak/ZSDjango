from django.db import models


class Aktualita(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Teachers(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    linkedin = models.CharField(max_length=200)
