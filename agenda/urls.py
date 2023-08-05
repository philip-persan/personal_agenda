from django.urls import path

from . import views

app_name = 'agenda'

urlpatterns = [
    path('create/', views.ContatoCreateView.as_view(), name='create'),
    path('list/', views.ContatoListView.as_view(), name='list'),
    path('update/<int:id>/', views.ContatoUpdateView.as_view(), name='update'),
    path('delete/<int:id>/', views.ContatoDeleteView.as_view(), name='delete'),
    path('gerador/', views.GeradorDeContatoView.as_view(), name='gerador'),
]
