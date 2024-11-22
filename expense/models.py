from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(
            0.01, message="Expense amount must be positive")]
    )
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
