from django.contrib import admin
from bookmarkmakerapp.models import bookmarkMakertable

class bookmarkMakertableAdmin(admin.ModelAdmin):
    list_display=['site_name',"site_url"]

admin.site.register(bookmarkMakertable,bookmarkMakertableAdmin)