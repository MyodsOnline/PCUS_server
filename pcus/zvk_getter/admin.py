from django.contrib import admin
from .models import CSV_data, ZVK_data, Station, Block, Generator

# Register your models here.
admin.site.register(CSV_data)
admin.site.register(ZVK_data)
admin.site.register(Station)
admin.site.register(Block)
admin.site.register(Generator)
