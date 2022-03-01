from django import forms


class FeedbackForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={
        'class': 'form-control'}))

    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
        'class': 'form-control', 'rows': 5}))


class MailingForm(forms.Form):
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={
        'class': 'form-control'}))








