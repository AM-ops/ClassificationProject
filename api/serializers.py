from rest_framework import serializers
from .models import Classification, ClassificationItem
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

# class ItemListSerializer(serializers.ListSerializer):
#     def create(self, validated_data):
#         items = [ClassificationItem(**item) for item in validated_data]
#         return ClassificationItem.objects.bulk_create(items)

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'

class ClassificationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationItem
        # list_serializer_class = ItemListSerializer
        fields = '__all__'

