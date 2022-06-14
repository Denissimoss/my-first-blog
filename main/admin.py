from django.contrib import admin
from .models import TableBase
from .models import UserCreationForm
admin.site.register(TableBase)
admin.site.register(UserCreationForm)