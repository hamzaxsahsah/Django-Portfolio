from django.db import models

# Create your models here.
class Education(models.Model):
	school_name = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	diploma_name = models.TextField()


class Technology(models.Model):
	name=models.TextField()

class Project(models.Model):
	name=models.TextField()
	technologies = models.ManyToManyField(Technology)
	description = models.TextField()
	source = models.TextField(blank=True)
	live_example = models.TextField(blank=True)


class Prize(models.Model):
	name=models.TextField()
	date = models.DateField()
	description = models.TextField()


class Persone(models.Model):
	name = models.TextField()
	role = models.TextField()
	description = models.TextField()
	resume = models.TextField()
	contact = models.TextField()
	email = models.TextField()
	github = models.TextField()
	linkedin = models.TextField()
