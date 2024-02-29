from django.contrib import admin
from .models import *
from .models import about

# Register your models here.


admin.site.register(CompanyInformation)

admin.site.register(Category)

admin.site.register(Product)

admin.site.register(about)

admin.site.register(contact)
