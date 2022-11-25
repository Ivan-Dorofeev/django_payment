from django.contrib import admin
from django.urls import path
from .views import buy, main, item_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('buy/<int:id_product>', buy, name='buy'),
    path('item/<int:id_product>', item_info, name='item_info'),
]
