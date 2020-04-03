from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Product


class ProductList(View):
    template_name = 'products/list.html'

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        return render(request, self.template_name, {'products': products})


class ProductDetail(View):
    template_name = 'products/detail.html'

    def get(self, request, id, *args, **kwargs):
        product = get_object_or_404(Product, pk=id)
        return render(request, self.template_name, {'product': product})
