from django.db import models

class paras(models.Model):
	name = models.CharField(max_length = 140)
	def __str__(self):
		return self.name

class jain(models.Model):
	hits = models.IntegerField(default=0)
# Create your models here.
