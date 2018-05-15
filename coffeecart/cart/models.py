from django.db import models

class Snacks(models.Model):
	name = models.CharField(max_length=40)
	ingredients = models.TextField()
	recommendations = models.TextField()

	def __str__(self):
		return '<ID: {}, Name: {}>'.format(self.id, self.name)

class Drinks(models.Model):
	name = models.CharField(max_length=40)
	ingredients = models.TextField()
	recommendations = models.TextField()


	def __str__(self):
		return '<ID: {}, Name: {}>'.format(self.id, self.name)

