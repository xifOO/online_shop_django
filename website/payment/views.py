from django.shortcuts import render, redirect


def un_success(request):
    return render(request, 'un_success.html')


def success(request):
    return render(request, 'success.html')



