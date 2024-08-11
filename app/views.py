from django.shortcuts import render

from app.forms import LastActiveForm
from app.models import ParametrT


# Create your views here.

def index(request):
    items = ParametrT.objects.all()
    if request.method == 'GET':
        return render(request, 'temp_log.html', {"items": items, 'form': LastActiveForm()})
    else:
        answer_form = LastActiveForm(request.POST)
        print(answer_form.data)
        return render(request, 'temp_log.html', {"items": items, 'form': LastActiveForm()})
