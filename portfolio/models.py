from django.db import models
import base64

# Create your models here.
class Education(models.Model):
	school_name = models.TextField()
	start_date = models.DateField()
	end_date = models.DateField()
	diploma_name = models.TextField()


class Technology(models.Model):
	name=models.TextField()



class DImage(models.Model):
	name=models.TextField()
	image = models.ImageField(upload_to="media")
	picture = models.TextField(null=True, blank=True)


	

	def save(self, *args, **kwargs):
		if self.image:
        	# Ensure the image is read and converted to base64 properly
			self.picture = f"data:image/{self.image.name.split('.')[-1]};base64,{base64.b64encode(self.image.read()).decode('utf-8')}"
			print("Base64 Image:", self.picture)
		super(DImage, self).save(*args, **kwargs)

    


class Project(models.Model):
	name=models.TextField()
	technologies = models.ManyToManyField(Technology)
	description = models.TextField()
	source = models.TextField(blank=True)
	live_example = models.TextField(blank=True)
	articale = models.TextField(blank=True)
	images = models.ManyToManyField(DImage)

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
