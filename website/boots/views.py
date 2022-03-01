from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Product
from cart.cart import Cart


def order_app(request):
    """Главная страница"""
    return render(request, 'main_app.html')


def boots_app(request):
    """Вывод товаров по категории"""
    objects_list = Product.objects.filter(category='Boots')
    paginator = Paginator(objects_list, 6)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        orders = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        orders = paginator.page(paginator.num_pages)
    return render(request, 'boots.html', {'orders': orders, 'page': page})


def football_form_app(request):
    """Вывод товаров по категории"""
    objects_list = Product.objects.filter(category='Form')
    paginator = Paginator(objects_list, 6)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        orders = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        orders = paginator.page(paginator.num_pages)
    return render(request, 'footballform.html', {'orders': orders, 'page': page})


def goalkeeper_form_app(request):
    """Вывод товаров по категории"""
    objects_list = Product.objects.filter(category='GoalKeeper')
    paginator = Paginator(objects_list, 6)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        orders = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        orders = paginator.page(paginator.num_pages)
    return render(request, 'goalkeeperform.html', {'orders': orders, 'page': page})


def project_info(request):
    """Функция, выводящая информацию о проекте"""
    return render(request, 'project_info.html')


def boots_detail(request, slug):
    """Функция, выводящая информацию об отдельном товаре"""
    boots = get_object_or_404(Product, slug=slug)
    context = {
        'boots': boots,
    }
    return render(request, 'boots_detail.html', context=context)


def football_form_detail(request, slug):
    """Функция, выводящая информацию об отдельном товаре"""
    football_form = get_object_or_404(Product, slug=slug)

    context = {
        'foot_form': football_form,
    }
    return render(request, 'football_form_detail.html', context=context)


def goalkeeper_form_detail(request, slug):
    """Функция, выводящая отдельный товар"""
    goalkeeper_form = get_object_or_404(Product, slug=slug)

    context = {
        "goalkeeper_form": goalkeeper_form,
    }
    return render(request, 'goalkeeper_form_detail.html', context=context)


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)



