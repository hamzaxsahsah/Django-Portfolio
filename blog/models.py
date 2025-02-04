from django.db import models
from portfolio.models import DImage
import datetime

# Create your models here.


class Blog(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.TextField()
    hex_color = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.TextField()
    content = models.TextField()
    images = models.ManyToManyField(DImage)
    Blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    # Automatically sets the creation date
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    @property
    def time_from_creation(self):
        time_now = datetime.datetime.now()
        time_create = self.created_at
        years = time_now.year - time_create.year
        if years > 0:
            return f"{years} year{'s' if 1!=years  else ''} ago"
        months = time_now.month - time_create.month
        if months > 0:
            return f"{months} month{'s' if 1!=months  else ''} ago"
        days = time_now.day - time_create.day
        if days > 0:
            return f"{days} day{'s' if 1!=days  else ''} ago"
        hours = time_now.hour - time_create.hour
        if hours > 0:
            return f"{hours} hour{'s' if 1!=hours  else ''} ago"
        minutes = time_now.minute - time_create.minute
        if minutes > 0:
            return f"{minutes} minute{'s' if 1!=minutes  else ''} ago"
        if seconds > 0:
            return f"{seconds}s ago"
