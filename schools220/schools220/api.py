from rest_framework.routers import DefaultRouter
from schoolsite220.api_views import NewsViewset

router = DefaultRouter()

router.register('news', NewsViewset, basename='news',)
