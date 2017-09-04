from django.contrib import admin
import models

# Register your models here.

admin.site.register(models.Circunscripcion)
admin.site.register(models.Partido)

class ResultadoInLine(admin.TabularInline):
    model = models.Resultado

class AdminMesa(admin.ModelAdmin):
    inlines = [ResultadoInLine]

admin.site.register(models.Mesa, AdminMesa)