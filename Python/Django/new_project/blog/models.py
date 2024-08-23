from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if a user is deleted then its data will be deleted but vice-verse not true
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # Dunder(means double underscore) str method
    def __str__(self):
        return self.title
    
    
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    