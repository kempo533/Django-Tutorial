from django.shortcuts import render, redirect

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def register(request):
    if request.method == 'POST':
        pass
        return redirect(request, 'accounts/register.html')
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')