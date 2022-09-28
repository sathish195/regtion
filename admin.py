from django.contrib import admin
from .models import Reg

# Register your models here.
class RegAdmin(admin.ModelAdmin):
    list_display = ['username','password','con_password','first_name','last_name','mobileno']
    list_filter = ['username','last_name']
    class Meta:
        model=Reg
admin.site.register(Reg,RegAdmin)
