from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Classification, ClassificationItem
from .serializers import ClassificationSerializer, ClassificationItemSerializer

# Create your views here.
@csrf_exempt
def classification_list(request):
    if request.method == 'GET':
        classified = ClassificationItem.objects.all()
        serializer = ClassificationItemSerializer(classified, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassificationItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)