from django.urls import path
from .views import ProductList, ProductDetail

app_name='products'

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<int:id>/', ProductDetail.as_view(), name='detail')
]