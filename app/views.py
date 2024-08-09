from django.shortcuts import render

from app.models import ParametrT


# Create your views here.

def index(request):
    items = ParametrT.objects.all()
    return render(request, 'temp_log.html', {"items": items})
