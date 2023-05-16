
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings

# Create your models here.



class Turf(models.Model):
    title  = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, default=False) 
    turf_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Turf, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title

        


