from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import CategoryViewSet, TicketViewSet

router = DefaultRouter()
router.register("tickets", TicketViewSet, basename="ticket")
router.register("categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
