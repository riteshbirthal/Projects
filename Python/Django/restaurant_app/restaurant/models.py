from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
# Create your models here.


class table(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.name


class timings(models.Model):
    pass
    
    
class reservation_detail(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    table = models.CharField(max_length=50, blank=False)
    timing = models.CharField(max_length=50, blank=False)
    booking_time = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("reservation-detail", kwargs={"pk": self.pk})


class booking_detail(models.Model):
    name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(max_length=11, blank=False)
    booking_time = models.DateField(default=timezone.now)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("reservation-detail", kwargs={"pk": self.pk})
    

class FoodType(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class food(models.Model):
    class category_choices(models.TextChoices):
        Indian = "Indian"
        Italian = "Italian"
        Other = "Other"
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(default='default_food.jpg', upload_to='food_pics')
    food_id = models.CharField(max_length=100, unique=True, blank=False)
    # food_categories = [ (x, x) for x in list(FoodType.objects.all())]
    # category = models.CharField(max_length=20, choices=food_categories)
    category = models.CharField(max_length=20, choices=category_choices.choices)
    # Dunder(means double underscore) str method
    def __str__(self):
        return f"{ self.name } {self.food_id}"
    
    def get_absolute_url(self):
        return reverse("food-detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, related_name='food_items')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    food_id = models.CharField(default='1', max_length=100, unique=True, blank=False)
    
    def __str__(self):
        return self.name


