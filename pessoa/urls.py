from django.urls import path
from .views import ListaPessoaViews

urlpatterns = [
    path('',ListaPessoaViews.as_view(), name='pessoa.index'),
]
