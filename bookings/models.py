


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=100, default="ALI'S FOOD")
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    max_capacity = models.IntegerField()

class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.CharField(max_length=10)
    capacity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])

class Menu(models.Model):
    CATEGORY_CHOICES = [
        ('APP', 'Appetizer'),
        ('MAIN', 'Main Course'),
        ('DESS', 'Dessert'),
        ('BEV', 'Beverage'),
    ]
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    is_available = models.BooleanField(default=True)

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    number_of_guests = models.IntegerField()
    special_requests = models.TextField(blank=True)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    special_instructions = models.TextField(blank=True)