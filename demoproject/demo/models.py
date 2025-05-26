from django.db import models

# Create your models here.
class table(models.Model):
    name=models.CharField(max_length=50)
    website=models.URLField(max_length=100)

    def __str__(self):
        return self.name