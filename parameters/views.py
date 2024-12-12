from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from parameters.forms import CreateUserForm, ParametersForm, EditParametersForm
from parameters.models import Parameter


# Create your views here.
@login_required
def home(request):
    try:
        if request.user.is_staff:
            parameters = Parameter.objects.select_related('user').all().order_by('compID')
        else:
            parameters = Parameter.objects.select_related('user').filter(user=request.user).order_by('compID')

        # Prepare context for rendering
        context = {'parameters_list': parameters}
        return render(request, "home.html", context)
    except Exception as e:
        print(e)
        return render(request, "home.html")


def login_user(request):
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


def logout_user(request):
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
        form = ParametersForm()
        return render(request, 'parameter_create.html', {'form': form})
    else:
        try:
            form = ParametersForm(request.POST)
            if form.is_valid():
                parameter = form.save(commit=False)
                parameter.user = request.user
                parameter.save()
                messages.success(request, f'Parameter created successfully for CompID: {form.cleaned_data["compID"]}')
                return redirect('home')
            else:
                return render(request, 'parameter_create.html', {'form': form, 'error': 'Invalid form data.'})
        except Exception as e:
            return render(request, 'parameter_create.html', {'form': form, 'error': f'Error: {str(e)}'})


@login_required
def parameter_detail(request, parameter_id):
    if request.method == 'GET':
        parameter = get_object_or_404(Parameter, pk=parameter_id)
        form = EditParametersForm(instance=parameter)
        return render(request, 'parameter_detail.html', {'parameter': parameter, 'form': form})
    else:
        try:
            parameter = get_object_or_404(Parameter, pk=parameter_id)
            form = ParametersForm(request.POST, instance=parameter)
            form.save()
            messages.success(request, 'Parameter updated\\nCompID: ' + form.cleaned_data.get('compID'))
            return redirect('home')
        except ValueError:
            return render(request, 'parameter_detail.html', {'parameter': parameter, 'form': form,
                                                             'error': 'Error updating parameter'})


@login_required
def parameter_delete(request, parameter_id):
    parameter = get_object_or_404(Parameter, pk=parameter_id)
    parameter.delete()
    messages.success(request, "Parameters deleted\\nfor CompID: " + parameter.compID)
    return redirect('home')
