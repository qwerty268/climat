from django.shortcuts import render


# Create your views here.
from app.models import ParametrT


def index(request):
    items = ParametrT.objects.all()
    return render(request, 'temp_log.html', {"items": items})
