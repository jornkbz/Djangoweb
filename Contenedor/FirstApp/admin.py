from django.contrib import admin
from .models import AutorDb, FraseDb
# Register your models here.

class FraseInline(admin.TabularInline):
    model = FraseDb
    extra = 1


class AutorAdmin(admin.ModelAdmin):
    fields = ["nombre","fecha_nacimiento", "fecha_fallecimiehto", "profesion", "nacionalidad"]
    list_display = ["Nombre", "fecha_nacimiento"]


    inlines = [FraseInline]

admin.site.register(AutorDb, AutorAdmin)


@admin.register(FraseDb)
class FraseAdmin(admin.ModelAdmin):
    filds = ["cita", "autor_fk"]
    list_display = ["cita"]