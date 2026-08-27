from django.shortcuts import render

from .models import Ticket


def ticket_list(request):
    tickets = Ticket.objects.select_related("category").order_by("-created_at")
    return render(request, "tickets/ticket_list.html", {"tickets": tickets})
