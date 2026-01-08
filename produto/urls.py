from django.urls import path
from . import views

app_name = 'produto'

urlpatterns = [
    path('', views.ListaProdutos.as_view(), name="lista"),
    path('busca/', views.Busca.as_view(), name="busca"),
    path('carrinho/', views.Carrinho.as_view(), name="carrinho"),
    path('resumodacompra/', views.ResumoDaCompra.as_view(), name="resumodacompra"),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), name="adicionaraocarrinho"),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(), name="removerdocarrinho"),
    path('produto/<slug:slug>/', views.DetalheProduto.as_view(), name='detalhe'),
]
