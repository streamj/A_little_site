from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year,
                               self.pub_date.month,
                               self.slug)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]
