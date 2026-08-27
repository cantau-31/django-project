from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Category, Ticket


class TicketAPITests(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="API", description="Tickets liés à l'API")
        self.user = get_user_model().objects.create_user(username="alice", password="pass12345")

    def authenticate(self):
        response = self.client.post(
            "/api/token/", {"username": "alice", "password": "pass12345"}, format="json"
        )
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['access']}")

    def test_list_tickets_without_auth(self):
        response = self.client.get("/api/tickets/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ticket_without_auth_is_rejected(self):
        response = self.client.post(
            "/api/tickets/",
            {"title": "Bug", "description": "Un bug", "priority": "LOW", "category": self.category.id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_high_priority_requires_detailed_description(self):
        self.authenticate()
        response = self.client.post(
            "/api/tickets/",
            {
                "title": "Panne critique",
                "description": "trop court",
                "priority": "HIGH",
                "category": self.category.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_high_priority_with_detailed_description_is_created(self):
        self.authenticate()
        response = self.client.post(
            "/api/tickets/",
            {
                "title": "Panne critique",
                "description": "Description suffisamment détaillée pour un ticket HIGH.",
                "priority": "HIGH",
                "category": self.category.id,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ticket.objects.count(), 1)
