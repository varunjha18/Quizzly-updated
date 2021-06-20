from django.contrib import admin
from .models import forum,message
# Register your models here.

class mesAdmin(admin.ModelAdmin):
    
    list_display=('id','sender_name','content')
    # list_display_links=('car_title',)
    # list_editable= ('is_featured',)
    # search_fields=("first_name","last_name",'id')
    # list_filter=("first_name","last_name",'designation')




admin.site.register(forum)
admin.site.register(message,mesAdmin)