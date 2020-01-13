from datetime import datetime

from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from portfolio_App.forms import *
from portfolio_App.models import *

def credenciais(request):
    form = VisitanteForm()
    data = data = datetime.now()
    if request.method == 'POST':
        form = VisitanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('index'))
        else:
            HttpResponse('Deu errado!')
    return render(request, 'credenciais.html', locals())

def index(request):
    pessoa = Pessoa.objects.all()
    post = Post.objects.all()
    portifolio = Portifolio.objects.all()
    curso_tec = Curso_tec.objects.all()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['matheus.bertoldosi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, 'index.html', locals())

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


def blog(request, id):
    pessoa = Pessoa.objects.all()
    post = Post.objects.get(id=id)
    return render(request, 'blog.html', locals())


