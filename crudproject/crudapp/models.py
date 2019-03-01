from django.db import models

# model for contact
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=256, unique=True)
    phone_number = models.IntegerField(default=0)

    def __str__(self):
        return self.name