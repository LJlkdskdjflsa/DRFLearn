from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CreateCategoryAPIView.as_view(), name='create-category'),
    path('list', views.ListCategoryAPIView.as_view(), name='list-category')

]