from django.db import models

class paras(models.Model):
	Spoj_Handle = models.CharField(max_length = 140)
	def __str__(self):
		return self.Spoj_Handle

class jain(models.Model):
	hits = models.IntegerField(default=0)
# Create your models here.
