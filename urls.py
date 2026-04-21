from django.contrib import admin
from django.urls import path
from core.views import saludo  # Aquí le decimos que traiga tu mensaje

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo),  # Esta línea dice: "En la página principal, muestra el saludo"
]