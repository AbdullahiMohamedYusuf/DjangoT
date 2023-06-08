from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    type = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.type

class Shoe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    imgUrl = models.TextField(default='')
    discription = models.TextField(max_length=200, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    body = models.TextField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body


class Purchase(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.shoe.name