from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Socials(models.Model):
    social_media = models.CharField(max_length=200)
    link_to = models.TextField()
    image = models.ImageField(upload_to='socials/images/')
    def __str__(self):
        return self.social_media
    def summary(self):
        return self.image[:200]
