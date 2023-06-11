from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Spend(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    Creation = models.DateTimeField(auto_now_add=True)
    Creation_date = models.DateField(default=date.today, null=True, blank=True)
    amount = models.IntegerField()
    category_choices = [
        ('Meals', '餐飲費'),
        ('transportation', '交通'),
        ('groceries', '購物'),
        ('entertainment', '娛樂'),
        ('apparel', '衣服'),
        ('Pay', '繳費'),
        ('other', '其他'),
    ]
    category = models.CharField(max_length=20, choices=category_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}-{self.title}'