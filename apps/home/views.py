# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404, resolve_url
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


def landing(request):
    apps = Application.objects.all()
    categories = Category.objects.all()
    ctx = {'apps': apps, 'categories': categories}
    return render(request, 'home/landing.html', ctx)

def profile(request):
    apps = Application.objects.filter(user=request.user).all()
    categories = Category.objects.all()
    ctx = {'apps': apps, 'categories': categories}
    return render(request, 'home/profile.html', ctx)

@login_required(login_url="/login/")
def profileedit(request):
    context = {'segment': 'Profile Edit'}
    profile = Profile.objects.filter(user=request.user).last()
    form = ProfileForm(instance =profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            messages.success(request, 'Profile Updated.')
            return redirect('view_profile')
        else:
            messages.error(request, 'Profile could not be updated.')
    context['form'] = form
    html_template = loader.get_template('home/edit_profile.html')
    return render(request, 'home/edit_profile.html', context=context)

@login_required(login_url="/login/")
def add_software(request):
    is_dev = request.user.groups.filter(name='developer').exists()
    print(is_dev)
    if is_dev:
        context = {'segment': 'newupload'}
        form = ApplicationForm()
        if request.method == 'POST':
            form = ApplicationForm(request.POST, request.FILES)
            if form.is_valid():
                soft = form.save(commit=False)
                soft.developer_name = request.user
                soft.save()
                messages.success(request, 'Application Successfully added.')
                return redirect('all_software')
            else:
                messages.error(request, 'Application not added.')
        context['form'] = form
        html_template = loader.get_template('home/add_software.html')
        return render(request, 'home/add_software.html', context=context)
    else:
        messages.error(request, 'You are not a developer. request admin.')
        return redirect('all_software')

def view_all_software(request):
    apps = Application.objects.all()
    categories = Category.objects.all()
    ctx = {'apps': apps, 'categories': categories}
    return render(request, 'home/all_software.html', ctx)

def download(request, id):
    app = get_object_or_404(Application, pk=id)
    return redirect(app.setup.url)

@login_required(login_url="/login/")
def view_all_users(request):
    if request.user.is_superuser and request.method =='POST':
        id = request.POST.get('id')
        user = User.objects.get(id=id)
        group = Group.objects.get(name='developer')
        user.groups.add(group)
        messages.success(request, 'User added to developer group.')
        return redirect('all_users')
    group = Group.objects.get(name='developer')
    users = User.objects.all()
    ctx = {'users': users}
    return render(request, 'home/all_users.html', ctx)


@login_required(login_url="/login/")
def view_dev_software(request):
    apps = Application.objects.filter(developer_name=request.user).all()
    ctx = {
        'apps': apps
    }
    return render(request, 'home/software_dev_list.html', ctx)


@login_required(login_url="/login/")
def edit_dev_software(request, id):
    # form
    app = Application.objects.filter(
        developer_name=request.user).filter(id=id).first()
    ctx = {
        'app': app,
        # 'form':form
    }
    return render(request, 'home/software_dev_list.html', ctx)

@login_required(login_url="/login/")
def feedback(request):
    context = {'segment': 'feedback'}
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.user = request.user
            feed.save()
            messages.success(request, 'Feedback successfully posted.')
            return redirect('/')
        else:
            messages.error(request, 'Feedback could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/feedback.html')
    return render(request, 'home/feedback.html', context=context)

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
