from django.db import models
from accounts.models import User
from menu.models import FoodItem

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fooditem = models.ForeignKey(FoodItem,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.email  + " " + self.fooditem.food_name + " " + str(self.quantity )


