from django.contrib import admin
from django.urls import path

from stripe_payment.stripe_payment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
]
