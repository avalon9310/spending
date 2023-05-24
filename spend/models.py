from django import forms
from django.db import models
from django.contrib.auth.models import User



class Spend(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    Creation_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category_choices = [
        ('Meals', '餐飲費'),
        ('transportation', '交通'),
        ('groceries', '購物'),
        ('entertainment', '娛樂'),
        ('apparel', '衣服'),
    ]
    category = models.CharField(max_length=20, choices=category_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)