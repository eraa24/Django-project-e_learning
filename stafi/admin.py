from django.contrib import admin
from .models import Profesori
from .models import Kurset
from .models import Subject

class ProfesoriAdmin(admin.ModelAdmin):
    list_display = ( 'emri', 'mbiemri', 'cel', 'email')


admin.site.register(Profesori, ProfesoriAdmin)


class KursetAdmin(admin.ModelAdmin):
    list_display = ('leksioni', 'petagogu', 'kredite')


admin.site.register(Kurset, KursetAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'description')

admin.site.register(Subject, SubjectAdmin)
