from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})