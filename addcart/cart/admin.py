from django.contrib import admin
from .models import product

class hello(admin.ModelAdmin):
    list_display=('No','Name','Catagory','Email','Contact')

admin.site.register(product,hello)
