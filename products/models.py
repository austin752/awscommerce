from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
import random
import os

from awscommerce.utils import unique_slug_generator


def get_filename_ext(filepath):
	base_name = os.path.basename(filepath)
	name, ext = os.path.splitext(base_name)
	return name, ext


def upload_image_path(instance, filename):
	new_filename = random.randint(1, 6854984951)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
	return 'products/{new_filename}/{final_filename}'.format(
				new_filename=new_filename,
				final_filename=final_filename)

# returns instance queryset objects
class ProductQuerySet(models.query.QuerySet):
	pass
	def featured(self):
		return self.filter(featured=True, active=True)

	def active(self):
		return self.filter(active=True)
	
	def search(self, query):
		lookups = (
					Q(title__icontains = query) |
					Q(description__icontains = query) |
					Q(price__icontains = query)|
					Q(tag__title__icontains=query)|
					Q(tag__slug__icontains=query)
		 )
		return self.filter(lookups).distinct()


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)
	
	#returns all active items
	def all(self):
		return self.get_queryset().active()
	
	#returns all featured items that are active
	def featured(self):
		return self.get_queryset().featured()
	
	def get_by_id(self, id):
		return self.get_queryset().filter(id=id)
	
	def search(self, query):
		return self.get_queryset().active().search(query)
	

class Product(models.Model):
	name = models.CharField(max_length=120)
	slug = models.SlugField(blank=True, unique=True)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=8, default=39.99)
	image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	
	objects = ProductManager()
	
	def  get_absolute_url(self):
		#return '/products/{slug}'.format(slug=self.slug)
		return reverse('products:detail', kwargs={'slug': self.slug})

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)
	
pre_save.connect(product_pre_save_receiver, sender=Product)