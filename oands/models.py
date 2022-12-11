from django.db import models

# Create your models here.
class Ocr(models.Model):
    # image = models.ImageField(upload_to='images/')
    image=models.BinaryField(max_length=200)

class Meta:
    model=Ocr
    fields=['image']