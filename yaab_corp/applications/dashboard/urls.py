from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'dashboard_app'

urlpatterns = [
    path("",views.DashboardView.as_view(), name="index"),
    path('preguntas-respuestas/',views.PreguntasRespuestas.as_view(),name='preguntas_respuestas'),
    path('productos/productos-gral/',views.ProductosView.as_view(),name='productos_gral'),
    ##### producto #####
    path("dashboard/productos/nuevo-producto/",views.CreateProductosView.as_view(),name="nuevo_productos"),
    path('dashboard/productos/editar-productos/<int:pk>/',views.EditarProducto.as_view(),name='editar_productos'),
    path('dashboard/productos/eliminar-productos/<int:pk>/',views.EliminarProducto.as_view(),name='eliminar_productos'),
    
    ##### producto #####
    ##### plazo #####
    path("dashboard/plazos/nuevo-plazo/", views.CreatePlazoView.as_view(), name="nuevo_plazo"),
    path("dashboard/plazos/editar-plazo/<int:pk>/", views.EditarPlazoView.as_view(), name="editar_plazo"),
    path("dashboard/plazos/eliminar-plazo/<int:pk>", views.EliminarPlazo.as_view(), name="eliminar_plazo"),
    ##### plazo #####
    
    ##### obtener el interes ###
    path('obtener-interes/', views.obtener_interes, name='obtener_interes'),
    path('obtener-plazo/', views.obtener_plazo, name='obtener_plazo'),
    ##### obtener el interes ###
    
    path("editar-usuario/<int:pk>", views.EditarUsuarioUsers.as_view(), name="editar_usuario"),
    path("terminos/", views.TerminosCondiciones.as_view(), name="terminos_condiciones"),
]
