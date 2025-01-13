from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","date","occupation")
    search_fields=("first_name","last_name","email","date","occupation")
    list_filter=("occupation","date")
    ordering=("first_name", )
    readonly_fields=("occupation",)
# Register your models here.
admin.site.register(Form,FormAdmin)
#username:kasak