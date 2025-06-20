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
        return Budget.objects.create(**validated_data)
    
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
    
class TransactionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Category.objects.all(), required=False)
    
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'category', 'amount', 
                  'payment_method', 'transaction_date',
                  'type', 'description', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        user = self.context['request'].user
        return Transaction.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        user = validated_data.pop('user', None)
        category = validated_data.pop('category', None)
        transaction = super().update(instance, validated_data)
        transaction.save()
        if user is not None:
            instance.user = user
        if category is not None:
            instance.category = category
        instance.save()
        return instance
    
class ExpenditureSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), required=False)
    transaction = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Transaction.objects.all(), required=False)
    budget = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Budget.objects.all(), required=False)
    
    class Meta:
        model = Expenditure
        fields = ['id', 'user', 'transaction', 'budget','amount', 'date']
    
    def validate(self, data):
        user = data.get('user')
        transaction = data.get('transaction')
        budget = data.get('budget')
        amount = data.get('amount')

        # Check user consistency
        if transaction.user != user:
            raise serializers.ValidationError("Transaction user does not match expenditure user.")
        if budget.user != user:
            raise serializers.ValidationError("Budget user does not match expenditure user.")

        # Check category type is expense
        if transaction.category.type != 'expense':
            raise serializers.ValidationError("Expenditure must be linked to an 'expense' category.")

        # Overspend check
        if amount > transaction.amount:
            raise serializers.ValidationError("Expenditure amount exceeds the linked transaction amount.")
        
