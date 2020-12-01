
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addItem/', views.AddItem, name='add'),
    path('list/', views.ListItem, name='listItem'),
    path('detail/<int:id>', views.DetailItem, name='detail')
]
