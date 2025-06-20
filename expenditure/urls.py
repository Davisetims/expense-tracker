from rest_framework.routers import DefaultRouter
from expenditure.views import CategoryViewSet, BudgetViewSet, TransactionViewSet, ExpenditureViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'budget', BudgetViewSet)
router.register(r'transaction', TransactionViewSet)
router.register(r'expenditure', ExpenditureViewSet)

urlpatterns = [   
    
]
urlpatterns += router.urls