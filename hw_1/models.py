from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey("self", on_delete=models.DO_NOTHING, default=True, blank=True)


# class Meta:
#      ordering = ['-name']
#
#
# def __str__(self):
#     return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)



class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)



