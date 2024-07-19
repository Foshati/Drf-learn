from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveSmallIntegerField()
    bio = models.TextField(max_length=120)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name
