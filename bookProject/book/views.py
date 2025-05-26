from django.shortcuts import render

#---------------------------------------------
#normal class based without serializer(model->admin->views->urls)
#we have to write conversion logic between JSON and Django model
"""from django.http import JsonResponse
from django.views import View
from .models import Book
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class BookView(View):

    def get(self, request):
        books = Book.objects.all().values()
        return JsonResponse(list(books), safe=False)

    def post(self, request):
        data = json.loads(request.body)
        book = Book.objects.create(
            title=data['title'],
            author=data['author'],
            published_date=data['published_date'],
            isbn=data['isbn']
        )
        return JsonResponse({'id': book.id, 'message': 'Book created'}, status=201)

@method_decorator(csrf_exempt, name='dispatch')
class BookDetailView(View):

    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            return JsonResponse({
                'title': book.title,
                'author': book.author,
                'published_date': str(book.published_date),
                'isbn': book.isbn
            })
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def put(self, request, pk):
        data = json.loads(request.body)
        try:
            book = Book.objects.get(id=pk)
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            book.published_date = data.get('published_date', book.published_date)
            book.isbn = data.get('isbn', book.isbn)
            book.save()
            return JsonResponse({'message': 'Book updated'})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return JsonResponse({'message': 'Book deleted'})
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)"""
#--------------------------------------------------------------------------------------------
#You don’t need to manually write conversion logic between JSON and your Django model.
#using serializer.py (model->admin->serializer->views->urls)
"""Using CLASS-BASED VIEW--APIView, we get full control over the request methods (get, post, put, etc.). So:
We explicitly call serializer.is_valid() and serializer.save().
This is more flexible than using GenericAPIView or ViewSet, where some things are handled automatically.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from django.http import Http404

class BookListCreateView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)#Serializes all records to JSON format (many=True means it’s a list of objects).
        return Response(serializer.data)#serializer is an object to access all the information we need to use dot data

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():#Validates the input data (checks for required fields, field types, etc.).
            serializer.save()#Saves the data to the database by creating a new Book object. if we call this method it will go to serializer.py method create or update
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) """
#--------------------------------------------------------------------------------------------
#using serializer.py (model->admin->serializer->views->urls)
#GenericAPIView-Purpose: GenericAPIView is an enhanced version of APIView that provides additional features to help with commonly needed behavior for working with database models. It comes with built-in support for querysets and serializers.
"""from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(GenericAPIView):
    queryset = Book.objects.all()#---------------if we are using GenericAPi view then we need to use queryset to get objects
    serializer_class = BookSerializer

    def get(self, request):
        books = Book.objects.all()
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(GenericAPIView):
    queryset = Book.objects.all()  # or you can override `get_queryset` method
    serializer_class = BookSerializer  # define the serializer

    def get(self, request, pk):
        book = self.get_object()  # Automatically retrieves object based on `pk`
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object()
        serializer = self.get_serializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
#--------------------------------------------------------------------------------------------
#using serializer.py (model->admin->serializer->views->urls)
# Implement the views using GenericAPIView + Mixins
"""When Mixins Might Be Overkill
If you just want a simple CRUD view with no custom logic, using predefined views like ListAPIView, CreateAPIView, etc., is shorter and cleaner."""
"""from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .models import Book
from .serializers import BookSerializer

class BookListCreateView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Book.objects.all()#self.get_queryset() internally to access the data
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class BookDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)"""
#-------------------------------------------------------------------------------------
#using serializer.py (model->admin->serializer->views->urls)
"""Use Concrete Generic Views if:
You want simple, fast, and DRY CRUD operations.
You don't need custom method handling (yet).
for mixins ✅ Yes (you must define get, post, etc.)	❌ No (method bindings are auto-handled)"""
"""from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView,
    UpdateAPIView, DestroyAPIView, ListCreateAPIView,
    RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
)
from .models import Book
from .serializers import BookSerializer

# List all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create a book
class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve a book
class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Update a book
class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Delete a book
class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# List and Create
class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve and Update
class BookRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve and Delete
class BookRetrieveDeleteView(RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve, Update and Delete
class BookRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer"""
#----------------------------------------------------------------------------------------
#ModelViewSet and routers-------------------------------------------------------------------------------------
#using serializer.py (model->admin->serializer->views->urls)
"""✅ You want clean, RESTful API routing with less boilerplate
✅ You prefer automatic URL handling via routers
✅ You're building standard CRUD APIs
Routers automatically generate URL patterns based on methods like .list(), .create(), .retrieve() etc., 
but only when those methods are part of a ViewSet"""
"""from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer"""
#----------------------------------------------------------------------------------------
# Library system --Authentication & Authorization

from rest_framework import generics, mixins, filters,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

#filter
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('id')
    serializer_class = BookSerializer

    # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'published_date']  # filter using exact match
    search_fields = ['title', 'author']              # partial search
    ordering_fields = ['published_date', 'title']

# List and Create View (Login Required)
# class BookListCreateView(mixins.ListModelMixin,
#                          mixins.CreateModelMixin,
#                          generics.GenericAPIView):
#
#     queryset = Book.objects.all()
#     #queryset = Book.objects.all().order_by('id')
#     serializer_class = BookSerializer
#     #permission_classes = [IsAuthenticated]
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# Retrieve, Update, and Delete (Admin Only)
class BookRetrieveUpdateDestroyView(mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

