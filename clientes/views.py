from django.shortcuts import render
from rest_framework import viewsets
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    