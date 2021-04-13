from django.contrib import admin
from .models import MyModel, NumberModel

admin.site.register(MyModel)

admin.site.register(NumberModel)