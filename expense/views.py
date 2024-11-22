from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Expense
from .serializers import ExpenseCategorySummarySerializer, ExpenseDateRangeSerializer, ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user')
        return self.queryset.filter(user_id=user_id) if user_id else self.queryset

    @action(detail=False, methods=['get'])
    def date_range(self, request):
        serializer = ExpenseDateRangeSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        start_date = serializer.validated_data['start_date']
        end_date = serializer.validated_data['end_date']
        user_id = serializer.validated_data['user']
        expenses = self.queryset.filter(
            user_id=user_id, date__range=[start_date, end_date])
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def category_summary(self, request):
        serializer = ExpenseCategorySummarySerializer(
            data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        month = serializer.validated_data['month']
        year = serializer.validated_data['year']
        user_id = serializer.validated_data['user']
        category_summary = self.queryset.filter(
            user_id=user_id, date__month=month, date__year=year
        ).values('category').annotate(total=Sum('amount'))
        return Response(category_summary)
