from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Filters

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return self.genre_name

class Key(models.Model):
    key = models.CharField(max_length=20)

    def __str__(self):
        return self.key



# Product
class Beat(models.Model):
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    audio = models.FileField()
    untagged_audio = models.FileField(null=True)
    cover = models.ImageField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True, null=True)
    tempo = models.PositiveIntegerField()
    key = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

# Feedback
class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()




# Order
# class Order(models.Model):
#     beat = models.ForeignKey(Beat, on_delete=models.CASCADE, max_length = 100, default=None)
#     date = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return self.beat.title