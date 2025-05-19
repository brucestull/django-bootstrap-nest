# areas\tests\test_area.py

import pytest
from django.urls import reverse
from areas.models import Area


@pytest.mark.django_db
def test_create_area(client):
    response = client.post(
        reverse("area_nest:area_create"),
        {"name": "New Zone", "parent_area": ""},  # noqa E501
    )
    assert response.status_code == 302
    assert Area.objects.filter(name="New Zone").exists()


@pytest.mark.django_db
def test_nested_areas(client):
    root = Area.objects.create(name="Root")
    child = Area.objects.create(name="Child", parent_area=root)
    grandchild = Area.objects.create(name="Grandchild", parent_area=child)

    assert grandchild.parent_area == child
    assert child.parent_area == root
    assert root.subareas.count() == 1
    assert child.subareas.count() == 1
    assert grandchild.subareas.count() == 0


@pytest.mark.django_db
def test_dashboard_view(client):
    Area.objects.create(name="TopLevel")
    url = reverse("area_nest:area_dashboard")
    response = client.get(url)
    assert response.status_code == 200
    assert b"TopLevel" in response.content
