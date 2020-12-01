from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('name/', views.nameView, name='name'),
    path('perfil2/<str:name>', views.perfilView2, name='perfilView2'),
    path('item-list/', views.itemsList, name='itemsList'),
    path('item-detail/<int:id>', views.itemDetail, name='itemDetail'),
]

