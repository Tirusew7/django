
from django.contrib import admin
from django.urls import path
from product.views import home, about, contact, product
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('product/',product, name='product')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
