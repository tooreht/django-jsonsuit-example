from django.contrib import admin
from django.db import models

from jsonsuit.widgets import JSONSuit

from .models import Fruit

# Register your models here.

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONSuit }
    }
