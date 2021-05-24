from django.urls import path, include
from .views import rout_list_view, rout_detail_view, rout_create_view, rout_update_view
from . import views

urlpatterns = [
    path('', rout_list_view.as_view(), name='routList-home'),
    path('rout/<int:pk>/', rout_detail_view.as_view(), name='rout-detail'),
    path('rout/new/', rout_create_view.as_view(), name='rout-create'),
    path('rout/edit/<int:pk>/', rout_update_view.as_view(), name='rout-update')
]