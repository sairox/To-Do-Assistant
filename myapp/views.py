from django.shortcuts import render # type: ignore

def home(request):
    return render(request, 'myapp/home.html')

def add_task(request):
    return render(request, 'myapp/add_task.html')

def view_task(request):
    return render(request, 'myapp/view_task.html')

def suggestions(request):
    return render(request, 'myapp/suggestions.html')

