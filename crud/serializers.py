from rest_framework import serializers
from .models import crudItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = crudItem
        fields = '__all__'
