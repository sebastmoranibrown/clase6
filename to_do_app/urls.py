from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('lists/', views.ListView, name='lists'),
    path('items/<int:list_id>', views.ListItemsViews, name="DonRamon"),
    path('change/<int:id>', views.ChangeStateItemViews, name="changeStateItem"),
    path('items2/<int:id>', views.ListItemsViewsOtherTemplate, name="changeStateItem2")
]
