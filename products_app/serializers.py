from rest_framework import serializers
from .models import Assortment, Division


class AssortmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assortment
        fields = ['name', 'measure_unit']


class DivisiontSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'
