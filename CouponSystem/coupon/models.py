from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.conf import settings

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from =  models.DateTimeField()
    valid_to = models.DateTimeField()
    num_available = models.IntegerField(default=1)
    num_used = models.IntegerField(default=0)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.code

    def can_use(self):
        is_active = True

        if self.is_active == False:
            is_active = False
        
        if self.num_used >= self.num_available and self.num_available != 0:
            is_active = False
        
        return is_active
    
    def use(self):
        self.num_used = self.num_used + 1

        if self.num_used == self.num_available:
            self.is_active = False
            
    
