from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'ecommerce/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'ecommerce/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'ecommerce/product_form.html'
    fields = ['name', 'price', 'description', 'stock_quantity']
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'ecommerce/product_form.html'
    fields = ['name', 'price', 'description', 'stock_quantity']
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'ecommerce/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

