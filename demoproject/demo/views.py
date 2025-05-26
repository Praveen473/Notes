from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .serializer import tableserial
from django.template.context_processors import request
from .models import table
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin
# Create your views here.
class call(View):
    def get(self,request):
        print("Hello World")
        return HttpResponse("Hello")
class TableView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = table.objects.all()
    serializer_class = tableserial

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)