from django.shortcuts import render
from .models import PlayerRun
from django.http import HttpResponseRedirect
from decimal import Decimal

def index(request):
    runs = PlayerRun.objects.order_by('-date')
    context = {
        'runs': runs
    }
    return render(request, 'player/index.html', context)


def save(request):
    if request.method == 'POST':
        pr = PlayerRun()
        pr.distance = Decimal(request.POST.get('distance'))
        pr.time = Decimal(request.POST.get('time'))
        pr.mass = Decimal(request.POST.get('mass'))
        pr.save()
        return HttpResponseRedirect('/')
    return render(request, 'player/save.html')
