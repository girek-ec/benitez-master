from django.urls import path
from . import views
from .views import *

app_name = 'shop'


urlpatterns = [
    path('colexin/', index_eraly, name='index_eraly'),
    path('colexin/tienda/', product_list, name='product_list'),
    path('colexin/tienda/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('colexin/tienda/<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
