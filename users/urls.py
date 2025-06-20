from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from users.views import UserViewSet, CustomObtainTokenPairView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path("token/request/", CustomObtainTokenPairView.as_view(), name="token_request"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"), 
    
]
urlpatterns += router.urls