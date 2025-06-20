from django.shortcuts import render
from rest_framework import viewsets, permissions
from expenditure.serializers import BudgetSerializer, CategorySerializer
from expenditure.models import Budget, Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
