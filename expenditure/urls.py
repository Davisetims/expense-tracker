from rest_framework.routers import DefaultRouter
from expenditure.views import CategoryViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)

urlpatterns = [   
    
]
urlpatterns += router.urls