from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)  # type: ignore
    email = models.CharField(max_length=122)  # type: ignore
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name