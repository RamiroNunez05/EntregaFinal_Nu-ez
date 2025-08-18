from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('crear-familiar/', views.crear_familiar, name='crear-familiar'),
        path('listar-familiares/', views.listar_familiares, name='listar-familiares'),

        path('compra/', views.CompraCreateView.as_view(), name='compra'),
        path('ultimas-compras/', views.CompraListView.as_view(), name='ultimas-compras'),
        path('detalle-compra/<int:pk>/', views.CompraDetailView.as_view(), name='detalle-compra'),
        path('editar/<int:pk>/', views.CompraUpdateView.as_view(), name='editar-compra'),
        path('eliminar-compra/<int:pk>/', views.CompraDeleteView.as_view(), name='eliminar-compra'),
        path('buscar-compras/', views.buscar_compras, name="buscar-compras"),

        path('reservar-vuelo/', views.reservar_vuelo, name="reservar-vuelo"),
        path('vuelos-reservados/', views.vuelos_reservados, name="vuelos-reservados"),
        path('buscar-vuelos/', views.buscar_vuelos, name="buscar-vuelos"),

        path('about/', views.about, name="about"),
]