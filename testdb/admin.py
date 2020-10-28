from django.contrib import admin
from .models import Teachers, Classes, Absents, Students, Records

admin.site.register(Teachers)
admin.site.register(Classes)
admin.site.register(Absents)
admin.site.register(Students)
admin.site.register(Records)
