
from django.db import models
from django.urls import reverse
from datetime import datetime
#from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
	title		 	= models.CharField(max_length=120)
	body 			= models.TextField(blank=True,null=True)
	Image 			= models.ImageField(upload_to='#', default='#')
	post_date 		= models.DateTimeField(default=datetime.now, blank=True)
	#slugfield		= models.SlugField()


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',args=(str(self.id)))