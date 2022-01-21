from unicodedata import name
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import RegisterUserViewSet, RegisterApiView
from articles.views import ArticleViewSet
router = DefaultRouter()
router.register(
    "v1/core/register", RegisterUserViewSet, basename="register"
)
router.register('v1/articles', ArticleViewSet, basename="articles")
# urlpatterns = [
#     path("v1/core/register",  RegisterApiView.as_view(), name='register'),
# ]