from django.urls import path
from .views import AvistamientosList,AvistamientosDestroy,AvistamientosUpdate,avistamientoForIdEspecie

urlpatterns = [
    path('avistamientos/', AvistamientosList.as_view(), name='avistamientos-list'),
    path('avistamientos/destroy/<int:pk>/', AvistamientosDestroy.as_view(), name='avistamientos-destroy'),
    path('avistamientos/update/<int:pk>/', AvistamientosUpdate.as_view(), name='avistamientos-update'),
    # categoria for id especie
    path('findavistamiento/<int:pk>/', avistamientoForIdEspecie.as_view(), name='avistamientoForIdEspecie'),
]
