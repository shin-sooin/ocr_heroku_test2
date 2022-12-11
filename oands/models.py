from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Ocr(models.Model):
    # image = models.ImageField(upload_to='images/')
    image=models.AutoField(max_length=200)
