from django.db import models
from django.urls import reverse\


# Create your models here.
class Projects(models.Model):
    title=models.CharField(max_length=50, unique=True)
    description=models.TextField(max_length=500)
    projectImg=models.ImageField(upload_to="images/projects", blank=True)
    link=models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description=models.CharField(max_length=250)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name

class Knowledge(models.Model):
    title=models.CharField(max_length=50, unique=True)
    slug=models.SlugField(max_length=50)
    level=models.FloatField()
    bar_level=models.CharField(max_length=3, default=0)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Experience(models.Model):
    
    title=models.CharField(max_length=50)
    company=models.CharField(max_length=50)
    current=models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    address=models.CharField(max_length=50)
    description=models.TextField(max_length=500)

    def __str__(self):
        return self.title