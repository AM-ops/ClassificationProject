from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Classification, ClassificationItem
from .serializers import ClassificationSerializer, ClassificationItemSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import ModelFormWithFileField, UpdateModelForm
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.files.storage import FileSystemStorage

#from django.db.models import Count



currUser = get_user_model()

# Create your views here.
class ClassificationView(viewsets.ModelViewSet):
    serializer_class = ClassificationSerializer
    queryset = Classification.objects.all()

class ClassificationItemView(viewsets.ModelViewSet):
    serializer_class = ClassificationItemSerializer
    queryset = ClassificationItem.objects.all()


@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST',])
def classification_list(request):
    if currUser is not None:
        username = currUser.objects.get(username=request.user.username)
        userid = currUser.objects.get(pk=request.user.pk).pk
    if request.method == 'GET':
        classified = Classification.objects.all().filter(user=username).order_by('file_name')
        serializer = ClassificationSerializer(classified, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        data['user'] = userid
        serializer = ClassificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST',])
def classificationitem_list(request):
    if request.method == 'GET':
        classified = ClassificationItem.objects.filter().order_by('item_type')
        serializer = ClassificationItemSerializer(classified, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassificationItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(['POST'])
def classificationitem_add(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClassificationItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(['PUT',])
def classificationitem_edit(request, pk):
    if request.method == 'PUT':
        try:
            item = ClassificationItem.objects.get(pk=pk)
        except ClassificationItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data = JSONParser().parse(request)
        data['id'] = item.pk
        serializer = ClassificationItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@permission_classes((IsAuthenticated,))
@api_view(['DELETE'])
def classificationitem_delete(request,pk):
    if request.method == 'DELETE':
        try:
            item = ClassificationItem.objects.get(pk=pk)
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ClassificationItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class ClassificationCreateView(LoginRequiredMixin,CreateView):
    form_class = ModelFormWithFileField
    template_name = 'createClass_form.html'
    model = Classification
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

@permission_classes((IsAuthenticated,))
class ClassItemDetail(APIView):
    """
    Retrieve, update or delete a Classification Item instance.
    """
    def get_object(self, pk):
        try:
            return ClassificationItem.objects.get(pk=pk)
        except ClassificationItem.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        items = self.get_object(pk)
        serializer = ClassificationItemSerializer(items)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ClassificationItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((IsAuthenticated,))
class ItemList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        items = ClassificationItem.objects.all()
        serializer = ClassificationItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ClassificationItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassificationListView(LoginRequiredMixin,ListView):
    template_name = 'class_list.html'
    context_object_name = 'list'

    def get_queryset(self):
        queryset = Classification.objects.all()
        username = currUser.objects.get(username=self.request.user.username)
        if username is not None:
            queryset = queryset.filter(user=username).order_by('file_name')
        return queryset

class ClassificationListDetailView(LoginRequiredMixin,DetailView):
    model = Classification
    context_object_name = 'detail'
    template_name = 'class_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClassificationListDetailView, self).get_context_data(**kwargs)
        queryset = ClassificationItem.objects.all()
        username = currUser.objects.get(username=self.request.user.username)
        if username is not None:
            queryset = ClassificationItem.objects.filter(item_type=self.object.pk)
            context['queryset'] = queryset
        return context

class ClassificationDeleteView(LoginRequiredMixin,DeleteView):
    model = Classification
    template_name = 'class_delete.html'
    success_url = reverse_lazy('api:class_list')

class ItemDeleteView(LoginRequiredMixin,DeleteView):
    model = ClassificationItem
    template_name = 'item_delete.html'
    success_url = reverse_lazy('api:class_list')

# class ItemsDetailView(LoginRequiredMixin,DetailView):
#     model = ClassificationItem
#     context_object_name = 'detail'
#     template_name = 'class_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super(ClassificationListDetailView, self).get_context_data(**kwargs)
#         queryset = ClassificationItem.objects.all()
#         username = currUser.objects.get(username=self.request.user.username)
#         if username is not None:
#             queryset = ClassificationItem.objects.filter(item_type=self.object.pk)
#             context['queryset'] = queryset
#         return context

class ItemUpdateView(LoginRequiredMixin,UpdateView):
    model = ClassificationItem
    form_class = UpdateModelForm
    template_name = "item_edit.html"
    success_url = reverse_lazy('api:class_list')
    context_object_name = 'list'

    # def get_object(self, queryset=None):
    #     return get_object_or_404(self.model, pk=self.request..pk)

    # def get(self, request, *args, **kwargs):
    #     self.referer = request.META.get("HTTP_REFERER", "")
    #     request.session["login_referer"] = self.referer
    #     return super().get(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     self.referer = request.session.get("login_referer", "")
    #     return super().post(request, *args, **kwargs)

    # def form_valid(self, form):
    #     pw = form.cleaned_data["password1"]
    #     if pw != "":
    #         self.object.set_password(pw)
    #     self.object.save()

    #     messages.info(self.request, _("Account info saved!"))

