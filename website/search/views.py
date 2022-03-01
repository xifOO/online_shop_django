from django.shortcuts import render
from django.views.generic import ListView
from boots.models import Product


class Search(ListView):
    """Поиск по сайту"""
    template_name = 'search.html'
    context_object_name = 'orders'

    def get_queryset(self):
        """Получаем введенную пользователем строку"""
        return Product.objects.filter(name__icontains=self.request.GET.get('s'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context