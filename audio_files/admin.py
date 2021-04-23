from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SongFiles)
admin.site.register(PodCastFiles)
admin.site.register(AudioBookFiles)