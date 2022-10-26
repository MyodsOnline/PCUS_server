from django.contrib import admin

# Register your models here.
from .models import PCUS, OBJ

admin.site.register(PCUS)
admin.site.register(OBJ)
