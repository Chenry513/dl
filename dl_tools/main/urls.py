# main/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api_views import ModelInfoViewSet, UserProfileView, UserRegistrationView, UserPreferenceCreateView, UserPreferenceListView, UserPreferenceUpdateView

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )

router = DefaultRouter()
router.register(r'models', ModelInfoViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.index, name='search'),
    path('profile/', views.index, name='profile'),
    path('api/', include(router.urls)),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    # path('api/register/', UserRegistrationView.as_view(), name='register'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/preferences/', UserPreferenceCreateView.as_view(), name='preferences'),
    path('api/preferences/list/', UserPreferenceListView.as_view(), name='preference-list'),
    path('api/preferences/<int:pk>/', UserPreferenceUpdateView.as_view(), name='preference-update'),

    path('set-csrf/', views.set_csrf_token, name='set-csrf-token'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('auth-check/', views.auth_check, name='auth-check'),

]