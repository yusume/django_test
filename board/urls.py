from django.urls import path
from . import views

urlpatterns =[
   path('list', views.list, name='list'),
   path('new', views.new, name='new'),
   path('edit/<int:pk>', views.edit, name='edit'),
   path('remove/<int:pk>', views.remove, name='remove'),
]
