"""
URL configuration for bookProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""from django.contrib import admin
from django.urls import path
from book.views import BookListCreateView,BookDetailView
#BookView, BookDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('books/', BookView.as_view()),
    #path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookDetailView.as_view()),
]#upto mixins and genericAPi"""

#for concreate class
"""from django.contrib import admin
from django.urls import path
from book.views import BookListCreateView,BookRetrieveUpdateDeleteView,BookListView,BookCreateView,BookRetrieveView,BookUpdateView,BookDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-rud'),

    # Optional: expose individual operations
    path('books/list/', BookListView.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('books/<int:pk>/retrieve/', BookRetrieveView.as_view()),
    path('books/<int:pk>/update/', BookUpdateView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteView.as_view()),
]"""

#modelvieset and routers
"""from django.urls import path, include
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet
router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
urlpatterns = [
    path('', include(router.urls)),
]"""

#authentication
from django.urls import path
from django.contrib import admin
from book.views import BookListCreateView, BookRetrieveUpdateDestroyView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListCreateView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view()),
    path('api-token-auth/', obtain_auth_token),  # to get the token
]


