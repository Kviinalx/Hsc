from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', inicio, name="inicio"),

    path('registrar/',registrar_m,name="registrar"),
    path('registrarse/',registrarse,name="registrarse"),

    #Pagina iniciar
    path('iniciar/',iniciar,name="iniciar"),
    
    #Valida usuario
    path('iniciarsesion/',iniciar_sesion,name ="iniciarsesion"),

    path('microfonos/',mostrarMic, name="mostrarMic"),
    path('microfonos/<int:id>',micro, name="micro")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)