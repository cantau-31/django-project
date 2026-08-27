from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Category, Ticket
from .serializers import CategorySerializer, TicketSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all().order_by("id")
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.select_related("category").all().order_by("id")
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
