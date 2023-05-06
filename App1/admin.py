from django.contrib import admin
from .models import Usuario, Vocalista, Guitarrista, Bandas, Avatar

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Vocalista)
admin.site.register(Guitarrista)
admin.site.register(Bandas)
admin.site.register(Avatar)
