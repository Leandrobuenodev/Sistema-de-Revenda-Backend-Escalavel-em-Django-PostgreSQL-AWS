from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        
    else: 
        user_form = UserCreationForm() # Instancia o formulário padrão de criação de usuário do Django.

    return render(request, 'register.html', {'user_form': user_form}) # Renderiza o template com os dados


def login_view(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, data=request.POST) 
        
        if login_form.is_valid():
            user = login_form.get_user() 
            
            if user is not None:
                login(request, user)
                return redirect('cars_list')
             
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list')