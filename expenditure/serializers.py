from rest_framework import serializers
from expenditure.models import Expenditure, Category, Transaction, Budget
from users.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Category.objects.all(), required=False)
    
    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'amount_planned_to_spend', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Budget.objects.create(user=user)
    
    def update(self, instance, validated_data):
        user = validated_data.pop('user', None)
        category = validated_data.pop('category', None)
        budget = super().update(instance, validated_data)
        budget.save()
        if user is not None:
            instance.user = user
        if category is not None:
            instance.category = category
        instance.save()
        return instance
