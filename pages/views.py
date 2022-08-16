from django.views.generic.base import TemplateView
# Create your views here.
 

class HomePage(TemplateView):
    template_name = 'home.html'