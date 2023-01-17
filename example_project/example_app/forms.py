from django import forms

from jsonsuit.widgets import JSONSuit, ReadonlyJSONSuit

from .models import Fruit


class FruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields =  '__all__'
        widgets = {
            'data': JSONSuit(),
        }


class ReadonlyFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields =  '__all__'
        widgets = {
            'data': ReadonlyJSONSuit(),
        }


class RandomJSONForm(forms.Form):
    data = forms.JSONField(widget=JSONSuit())


class RandomReadonlyJSONForm(forms.Form):
    data = forms.JSONField(widget=ReadonlyJSONSuit())
