from django.db import models
from django.contrib.auth.models import User
from restaurant.models import food
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11, null=False, blank=False, unique=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            

class UserCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(default="None", max_length=50)
    food_price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    food_image_url = models.CharField(default="", max_length=500)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"{self.user.username} {self.food_name}"
    
    def add(self, food_name, food_price, food_quantity, image_url):
        self.food_name, self.food_price, self.quantity, self.food_image_url = food_name, food_price, food_quantity, image_url
    
    def get_total_price(self):
        self.total = float(self.food_price) * float(self.quantity)
        return self.total
            
     
class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.TextField(default="")
    ordered_on = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username} on {self.ordered_on} of {self.total}"