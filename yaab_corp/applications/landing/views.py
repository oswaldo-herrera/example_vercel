from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class Landing(TemplateView):
    pass
landing_view=Landing.as_view(template_name='landing/landing.html')