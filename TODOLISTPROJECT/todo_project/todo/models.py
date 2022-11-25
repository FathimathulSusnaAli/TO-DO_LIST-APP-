from django.db import models
from django.utils import timezone
 
# Create your models here.
class TodoListItem(models.Model):
    content = models.TextField() 
    date=models.DateField(auto_now_add=True)
    
# Create your models here.