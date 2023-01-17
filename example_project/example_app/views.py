import json, os, requests

from django.conf import settings
from django.shortcuts import render

from .forms import FruitForm, ReadonlyFruitForm, RandomJSONForm, RandomReadonlyJSONForm
from .models import Fruit

# Create your views here.

def index(request):
    return render(request, 'example_app/index.html')    


def template_tags(request):
    with open(os.path.join(settings.BASE_DIR, 'example_app', 'static', 'json_samples', 'fruits.json')) as file:
        data = json.load(file)
    context = {'data': data}
    return render(request, 'example_app/template_tags.html', context)


def forms(request):
    context = {}

    fruit_form = FruitForm(request.POST or None, request.FILES or None, initial=dict(data={}), prefix='editable-fruit')

    if fruit_form.is_valid():
        fruit_form.save()

    context['fruit_form'] = fruit_form
    context['ro_fruit_form'] = ReadonlyFruitForm(instance=Fruit.objects.first(), prefix='readonly-fruit')

    random_json_form = RandomJSONForm(request.POST or None, request.FILES or None, prefix='editable-quote', initial=dict(data={}))

    quote = requests.get('https://dummyjson.com/quotes/random')
    context['random_ro_json_form'] = RandomReadonlyJSONForm(initial=dict(data=quote.json()), prefix='readonly-quote')

    context['random_json_form'] = random_json_form
    return render(request, 'example_app/form.html', context)
