from unicodedata import name
from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from taco.models import Alimento
from taco.serializers import AlimentoSerializer
import sqlite3
from rest_framework import filters
class AlimentoViewSet(viewsets.ModelViewSet):
    alimento =  Alimento.objects.all()
    queryset = alimento
    serializer_class = AlimentoSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields  = ['name']
    ordering_fields = ['name','kcal']
