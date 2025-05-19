# areas\models.py

from django.db import models
from django.urls import reverse


class Area(models.Model):
    name = models.CharField(max_length=100)
    parent_area = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="subareas",
        on_delete=models.CASCADE,  # noqa: E501
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("area_nest:area_dashboard")
