from rest_framework import serializers
from .models import Classification, ClassificationItem

class ClassificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classification
        fields = '__all__'

class ClassificationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassificationItem
        types = ClassificationSerializer(many=False, read_only=True)
        #fields = '__all__'
        exclude = []