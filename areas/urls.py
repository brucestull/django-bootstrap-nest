# areas\urls.py

from django.urls import path

from . import views

app_name = "area_nest"

urlpatterns = [
    path("", views.AreaDashboardView.as_view(), name="area_dashboard"),
    path("create/", views.AreaCreateView.as_view(), name="area_create"),
    path("<int:pk>/edit/", views.AreaUpdateView.as_view(), name="area_edit"),
]
