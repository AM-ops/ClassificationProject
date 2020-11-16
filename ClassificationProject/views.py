from django.views.generic import TemplateView
from django.shortcuts import render

class HomePage(TemplateView):
    """docstring for HomePage."""
    template_name = 'index.html'

class SuccessPage(TemplateView):
    template_name = 'success.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def handler404(request, exception):
       return render(request, '404.html')