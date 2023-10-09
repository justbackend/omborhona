from django.shortcuts import render, redirect
from django.contrib.auth import logout,login, authenticate
from django.views import View
from .models import *
# Create your views here.

class Login(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/bolimlar/")

        return redirect("/")




# def home(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         return redirect("/bolimlar/")
#     return render(request, 'home.html')

def bolimlar(request):
    return render(request, 'bulimlar.html')

class Logout(View):
    def get(self):
        logout(request)
        return redirect("/")

def logout_view(reqeust):
    logout(reqeust)
    return redirect("/")

class Products(View):
    def get(self, request):
        content = {
            "products": Mahsulot.objects.filter(ombor__username=request.user.username)
        }
        return render(request, 'products.html', content)
    def post(self, request):
        Mahsulot.objects.create(
            nom = request.POST['nom'],
            narx= request.POST['narx'],
            miqdor=request.POST['miqdor'],
            olchov=request.POST['olchov'],
            ombor=Ombor.objects.get(username=request.user.username),
            brand = request.POST['brand']
        )

        return redirect("/products/")

class Clients(View):
    def get(self, request):
        content = {
            "clients": Mijoz.objects.filter(ombor=request.user)
        }
        return render(request, 'clients.html', content)

def ochir(request, id):
    Mijoz.objects.get(id=id).delete()
    return redirect("/clients/")