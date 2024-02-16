from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404

from parameters.forms import CreateUserForm, ParametersForm
from parameters.models import Parameter


# Create your views here.
@login_required
def home(request):
    try:
        if request.user.is_staff:
            context = {'parameters_list': Parameter.objects.all()}
        else:
            context = {'parameters_list': Parameter.objects.filter(user=request.user)}
        return render(request, "home.html", context)
    except Exception as e:
        print(e)
        return render(request, "home.html")


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register_user(request):
    if not request.user.is_staff:
        return redirect('home')
    else:
        if request.user.is_staff:
            form = CreateUserForm()
            if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)

                    return redirect('login')

            context = {'form': form}
            return render(request, 'register.html', context)


@login_required
def parameter_create(request):
    if request.method == 'GET':
        return render(request, 'parameter_create.html', {
            'form': ParametersForm
        })
    else:
        try:
            form = ParametersForm(request.POST)
            new_parameter = form.save(commit=False)
            new_parameter.user = request.user
            new_parameter.save()
            return redirect('home')
        except ValueError:
            return render(request, 'parameter_create.html', {
                'form': ParametersForm,
                'error': 'Please provide valid data'
            })


@login_required
def parameter_detail(request, parameter_id):
    if request.method == 'GET':
        parameter = get_object_or_404(Parameter, pk=parameter_id)
        form = ParametersForm(instance=parameter)
        return render(request, 'parameter_detail.html', {'parameter': parameter, 'form': form})
    else:
        try:
            parameter = get_object_or_404(Parameter, pk=parameter_id)
            form = ParametersForm(request.POST, instance=parameter)
            form.save()
            return redirect('home')
        except ValueError:
            return render(request, 'parameter_detail.html', {'parameter': parameter, 'form': form,
                                                             'error': 'Error updating parameter'})
