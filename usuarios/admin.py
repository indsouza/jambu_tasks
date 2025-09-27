from django.contrib import admin
from .models import Perfil

@admin.register(Perfil)
class AdministradorPerfil(admin.ModelAdmin):
    list_display = ('usuario', 'bio')
    search_fields = ('usuario__username', 'usuario__first_name', 'usuario__last_name')
