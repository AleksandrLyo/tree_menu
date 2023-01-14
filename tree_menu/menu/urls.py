from django.urls import path
from django.views.generic import TemplateView
 
urlpatterns = [
    path('menu/', TemplateView.as_view(template_name="menu/index.html")),
]
