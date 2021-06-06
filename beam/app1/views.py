from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def Index(request):
#     return HttpResponse("<h1> Hello Worls !!! </h1>")


def view(request):
    if request.POST:
        val1 = request.POST['a1']
        val2 = request.POST['a2']

        print(val1, val2)
        var = int(val1) + int(val2)
        print(var)
        return render(request, 'hello.html', {'ans': var, 'val1': val1, 'val2': val2})
        
    return render(request, 'hello.html')


def index(request):
    return render(request, 'index.html')


def common(request):
    return render(request, 'common.html')


def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')