from django.db import models
from django.template.defaultfilters import slugify  
from django.urls import reverse

# Create your models here.
class Phone(models.Model):
    STOCK = 'Stock'
    NOTSTOCK = 'Out of stock'
    STATUS = [
        (STOCK , ('Stock')),
        (NOTSTOCK , ('Out of stock')),
    ]
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField()
    price = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    storage = models.IntegerField()
    ram = models.IntegerField()
    battery_capacity = models.IntegerField()
    screen_size = models.FloatField()
    os = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    camera = models.CharField(max_length=50)
    slug = models.SlugField(max_length=500,null=False, unique=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("article_detail", kwargs={"slug": self.slug})

    # def save(self, *args, **kwargs):  
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)


class Media(models.Model):
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='media')
    


class Review(models.Model):
    creator = models.CharField(max_length=500)
    body = models.TextField()
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)