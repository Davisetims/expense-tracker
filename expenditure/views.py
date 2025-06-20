from django.shortcuts import render
from rest_framework import viewsets, permissions
from expenditure.serializers import BudgetSerializer, CategorySerializer, TransactionSerializer,\
ExpenditureSerializer
from expenditure.models import Budget, Category, Transaction, Expenditure

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Transaction.objects.filter(user=user)
        return Transaction.objects.all()
    
class ExpenditureViewSet(viewsets.ModelViewSet):
    queryset = Expenditure.objects.all()
    serializer_class = ExpenditureSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Expenditure.objects.filter(user=user)
        return Expenditure.objects.all()

