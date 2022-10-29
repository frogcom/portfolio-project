from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    txt_short = models.TextField()
    github_url = models.TextField()
    live_url = models.TextField()
    pub_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/project/images/')
    # icon = models.ImageField(upload_to='media/project/icon/')
    # votes_total = models.IntegerField(default=1)
    # hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    # admin panel
    def __str__(self):
        return self.title

    def summary(self):
        return self.txt_short[:200]

    # pub_date_pretty
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')