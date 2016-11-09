from django.shortcuts import get_object_or_404, render

import os
import random

# Create your views here.

from .models import Mineral


def mineral_detail(request, name):
    mineral = get_object_or_404(Mineral, name=name)
    return render(request, 'minerals\mineral_detail.html', {'mineral': mineral,})


def random_mineral(request):
    mineral = random.choice(
        Mineral.objects.all()
    )
    image_filepath = os.path.join('assets\static\images', mineral.image_filename)
    return render(request, 'minerals\mineral_detail.html', {'mineral': mineral,})