from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/product/<int:id>', views.product, name='product')
]