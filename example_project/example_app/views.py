import json, os

from django.conf import settings
from django.shortcuts import render

# Create your views here.

def index(request):
    with open(os.path.join(settings.BASE_DIR, 'example_app', 'static', 'json_samples', 'fruits.json')) as file:
        data = json.load(file)
    context = {'data': data}
    return render(request, 'example_app/index.html', context)