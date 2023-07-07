from django.shortcuts import render, redirect
from .models import Projects, Profile, Firm
from .utils import search_projects, paginate_projects
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.http.response import HttpResponseNotFound
from .forms import CustomUserCreationForm, ProjectForm


def projects(request):
    pr, search_query = search_projects(request)
    custom_range, pr = paginate_projects(request, pr, 3)

    context = {
        'projects': pr,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'shop/projects.html', context)


def single_card(request, pk):
    card_obj = Projects.objects.get(id=pk)
    return render(request, 'shop/single-card.html', {'card': card_obj})


# def firm_info(request):
#     project = Projects.objects.get(id=1)
#     context = {'project': project}
#     return render(request, 'shop/footer.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except ObjectDoesNotExist:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, "Username or password is incorrect")

    return render(request, 'shop/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "User was logged out!")
    return redirect('projects')


def register_user(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'shop/login_register.html', context)


@login_required(login_url="login")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, 'shop/form-template.html', context)


@login_required(login_url="login")
def update_project(request, pk):
    project = Projects.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        # new_tags = request.POST.get('tags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            # for tag in new_tags:
            #     tag, created = Tag.objects.get_or_create(name=tag)
            #     print(tag)
            #     project.tags.add(tag.name)
            return redirect('projects')

    context = {'form': form}
    return render(request, 'shop/form-template.html', context)


@login_required(login_url="login")
def delete_project(request, pk):
    project = Projects.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'shop/delete.html', context)



