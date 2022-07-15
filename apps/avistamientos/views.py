from django.shortcuts import render
from .serializers import AvistamientosSerializer
from .models import Avistamientos
from rest_framework.generics import (ListCreateAPIView, DestroyAPIView,UpdateAPIView)
from rest_framework.response import Response

class AvistamientosList(ListCreateAPIView):
    queryset = Avistamientos.objects.all()
    serializer_class = AvistamientosSerializer

class AvistamientosDestroy(DestroyAPIView):
    queryset = Avistamientos.objects.all()
    serializer_class = AvistamientosSerializer

class AvistamientosUpdate(UpdateAPIView):
    queryset = Avistamientos.objects.all()
    serializer_class = AvistamientosSerializer


# avistamientoForIdEspecie
class avistamientoForIdEspecie(ListCreateAPIView):
    serializer_class = AvistamientosSerializer
    def get_queryset(self):
        idEspecie = self.kwargs['pk']
        especie = Avistamientos.objects.filter(especie=idEspecie)
        return especie