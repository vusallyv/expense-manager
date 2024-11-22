from rest_framework import serializers
from .models import Expense
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'user', 'title', 'amount', 'date', 'category']
        extra_kwargs = {
            'title': {'required': False},
            'amount': {'required': False},
            'date': {'required': False},
            'category': {'required': False},
            'user': {'required': False}
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ExpenseDateRangeSerializer(serializers.Serializer):
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def validate(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "start_date must be less than or equal to end_date")
        return data


class ExpenseCategorySummarySerializer(serializers.Serializer):
    month = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)])
    year = serializers.IntegerField(validators=[MinValueValidator(0)])
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
