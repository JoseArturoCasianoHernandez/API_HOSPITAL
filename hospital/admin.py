from django.contrib import admin
from hospital.models import Medico, Paciente, Historia, PacienteCama, Cama, Planta, VisitaMedica

# Register your models here.
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Historia)
admin.site.register(PacienteCama)
admin.site.register(Cama)
admin.site.register(Planta)
admin.site.register(VisitaMedica)
