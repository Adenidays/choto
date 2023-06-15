from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.id}-{self.name}-{self.surname}'

    def get_absolut_url(self):
        return f"/user/{self.id}"