import urllib
import json
import datetime
import requests
from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import SignupForm
from .models import User, Table, Month, Estate, Report


def check_modal(request):
    modal = request.session.get('modal', 'none')
    try: 
        del request.session['modal']
    except KeyError:
        pass
    return modal

def index(request, year=2023):
    modal = check_modal(request)
    table = Table.objects.filter(year=year)[0]
    months = table.months.all().order_by('order')
    context={'form': SignupForm(), 'modal': modal, 'months': months}
    return render(request, 'api/index.html', context)

def dashboard(request):
    modal = check_modal(request)
    estate_list = Estate.objects.all()
    context={'form': SignupForm(), 'modal': modal, 'estate_list': estate_list}
    return render(request, 'api/dashboard.html', context)

def change_currency(request):
    modal = check_modal(request)
    estate_list = Estate.objects.all()
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    if data:
        dollar = data['Valute']['USD']['Value']
        request.session['currency'] = dollar
    # context={'form': SignupForm(), 'modal': modal, 'estate_list': estate_list}
    return HttpResponseRedirect(reverse('index'))

def remain_currency(request):
    modal = check_modal(request)
    estate_list = Estate.objects.all()
    if request.session['currency']:
        del request.session['currency']
    # context={'form': SignupForm(), 'modal': modal, 'estate_list': estate_list}
    return HttpResponseRedirect(reverse('index'))

def searched(request):
    modal = check_modal(request)
    search_text = request.POST.get('search')
    estate_list = Estate.objects.filter(title__icontains=search_text)
    context={'form': SignupForm(), 'modal': modal, 'estate_list': estate_list}
    return render(request, 'api/dashboard.html', context)

def estate_object(request, pk):
    modal = check_modal(request)
    annoucement = Estate.objects.get(pk=pk)
    context={'form': SignupForm(), 'modal': modal, 'annoucement': annoucement}
    return render(request, 'api/object.html', context)

def report(request):
    modal = check_modal(request)
    reports = Report.objects.all()
    context={'form': SignupForm(), 'modal': modal, 'reports': reports}
    return render(request, 'api/report.html', context)

def contact(request):
    modal = check_modal(request)
    context={'form': SignupForm(), 'modal': modal}
    return render(request, 'api/contact.html', context)

def agreement(request, year=2023):
    return render(request, 'api/agreement.html', context={})

def login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        auth_login(request, user)
        return redirect('registered')
    else:
        request.session['modal'] = 'login'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))
    
def logout_view(request):
    logout(request)
    context = {}
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            auth_login(request, user)
            return redirect('registered')
        
    if request.user.is_authenticated:
        return reverse('index')
    else:
        request.session['modal'] = 'register'
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', 'index'))
    
@login_required
def registered(request):
    modal = check_modal(request)
    context = {'form': SignupForm(), 'modal': modal}
    return render(request, 'api/index.html', context)