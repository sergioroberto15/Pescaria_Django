from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import Pescaria
from .models import Pescado

admin.site.register(Pescaria)
admin.site.register(Usuario)
admin.site.register(Pescado)