from django.shortcuts import render
# Create your views here.
def  index(request):
    return render(request,'pages/index.html')

def  h1(request):
    return render(request, "pages/h1.html")

def  h2(request):
    return render(request, "pages/h2.html")

def  h3(request):
    return render(request, "pages/h3.html")

def  Scénario(request):
    return render(request, "pages/Scénario.html")

def  s1(request):
    return render(request, "pages/s1.html")




