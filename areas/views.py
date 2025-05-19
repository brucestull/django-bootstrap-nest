# areas\views.py

from django.views import generic

from .forms import AreaForm
from .models import Area


class AreaCreateView(generic.CreateView):
    model = Area
    form_class = AreaForm
    template_name = "areas/area_form.html"


class AreaUpdateView(generic.UpdateView):
    model = Area
    form_class = AreaForm
    template_name = "areas/area_form.html"


class AreaDashboardView(generic.TemplateView):
    template_name = "areas/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_areas = Area.objects.filter(parent_area__isnull=True)
        context["top_areas"] = top_areas
        return context
