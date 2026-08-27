from rest_framework import serializers

from .models import Category, Ticket


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "title",
            "description",
            "priority",
            "status",
            "created_at",
            "category",
        ]
        read_only_fields = ["id", "created_at"]

    def validate(self, data):
        priority = data.get("priority", getattr(self.instance, "priority", None))
        description = data.get(
            "description",
            getattr(self.instance, "description", ""),
        )

        if priority == "HIGH" and len(description or "") < 20:
            raise serializers.ValidationError(
                "Un ticket prioritaire doit avoir une description détaillée."
            )

        return data
