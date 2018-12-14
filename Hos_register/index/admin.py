from django.contrib import admin
from .models import *

class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('uname','workday','client')
    list_display_links = ('uname',)
    list_editable = ('workday','client')
    search_fields = ('uname',)
    list_filter = ('workday','client')
    fieldsets = (
        # 分组一
        (
            '基本选项',{
                'fields':('uname','client'),
            }
        ),
        # 分组二
        (
            '高级选项',{
                'fields':('workday','account','upwd'),
                'classes':('collapse',)
        }
        )
    )

# Register your models here.
admin.site.register(Doctors,DoctorsAdmin)
