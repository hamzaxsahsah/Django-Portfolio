from django.db import models

# Create your models here.

class Blog(models.Model):
	title = models.TextField()


class Post(models.Model):
	title = models.TextField()
	content = models.TextField()
	image = models.ImageField()
	Blog = models.ForeignKey(Blog,on_delete=models.PROTECT)

class Tag(models.Model):
	name = models.TextField()
	Post = models.ForeignKey(Post,on_delete=models.PROTECT)