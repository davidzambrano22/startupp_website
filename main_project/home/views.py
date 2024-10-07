from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from .models import Caterogy, Subcategory, Product
from django.views import generic

# Create your views here.


class HomePageView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Caterogy.objects.all()
        context['subcategories'] = Subcategory.objects.all()
        context['products'] = Product.objects.all()

        return context

    

class CategoryGenericListView(generic.ListView):
    model = Caterogy
    context_object_name = 'categories'
    template_name = 'category_list.html'


class CategoryDetailView(generic.DetailView):
    model = Caterogy
    context_object_name = 'category'
    template_name = 'category_detail.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['subcategories'] = Subcategory.objects.filter(category=self.object)
        return context
    

