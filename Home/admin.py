from django.contrib import admin
from .models import Slider

admin.site.register(Slider)


# admin.site.site_title = 'مدیریت کافی تن'
# admin.site.site_header = 'مدیریت کافی تن'

class CustomAdminSite(admin.AdminSite):
    class Media:
        css = {
            'all': ('styles/admin_style.css',)
        }

