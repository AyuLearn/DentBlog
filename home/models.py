from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=400)
    email = models.CharField(max_length=800)
    message = models.TextField()

    def __str__(self):
        return self.name + ' - ' +self.email

class Post(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(blank=True, upload_to='post_images')
    slug = models.CharField(max_length=900)
    body = models.TextField()
    dt = models.DateField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.title
    