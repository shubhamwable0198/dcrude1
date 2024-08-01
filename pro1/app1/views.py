from django.shortcuts import render, redirect
from . forms import CustomerForm
from . models import Customer
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/a2/lv/")
def addview(request):
    form = CustomerForm()
    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request, "app1/add.html",{"form": form})

@login_required(login_url="/a2/lv/")
def showview(request):
    obj = Customer.objects.all()
    return render(request, "app1/show.html", {"cust": obj})


def updateview(request, id):
    obj = Customer.objects.get(cid=id)
    form = CustomerForm(instance=obj)
    if request.method =="POST":
        form = CustomerForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/av/")

    return render(request, "app1/add.html", {"form": form})


def deleteview(request, pk):
    obj = Customer.objects.get(cid=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")

    return render(request, "app1/confirm.html", {"obj": obj})
