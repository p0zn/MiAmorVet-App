from django.contrib import admin
from .models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):

    list_display = ['name','genus','type','created_date']
    list_display_links = ['name','genus','type','created_date']
    search_fields = ['name','genus','type']
    list_filter = ['created_date']
    

    class Meta:
        model = Pet 
        
