from django.urls import path
from django.views.generic import TemplateView

app_name = 'meta'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index')
    path('signup' views.signup, name='signup'),
]