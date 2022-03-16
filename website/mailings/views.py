from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import FeedbackForm, MailingForm
from django.contrib import messages
from settings import temp


def feedback(request):
    """Обратная связь"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], temp.EMAIL_HOST_USER,
                   [temp.FEEDBACK_EMAIL], fail_silently=False)
            if mail:
                return redirect('mailings:feedbacks')
            else:
                messages.success(request, 'Произошла ошибка')
    else:
        form = FeedbackForm()
    return render(request, 'mail_send.html', {'form': form})


def mailing(request):
    """Рассылка"""
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            mail = send_mail('xifOO', 'Вы подписались на рассылку', temp.EMAIL_HOST_USER,
                   [form.cleaned_data['email']], fail_silently=False)
            if mail:
                return redirect('mailings:mailing')
            else:
                messages.success(request, 'Произошла ошибка')
    else:
        form = MailingForm()
    return render(request, 'mailing.html', {'form': form})