from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .forms import PetForm
from .models import Pet


def pets(request):

    keyword = request.GET.get("keyword")

    if keyword:
        pets = Pet.objects.filter(name__contains = keyword)
        return render(request,"pets.html",{"pets":pets})

    pets = Pet.objects.all()

    context = {
        "pets" : pets
    }

    return render(request,"pets.html",context)



def index(request):
    context = {

    }

    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

@login_required(login_url="user:login")
def dashboard(request):
    pets = Pet.objects.filter(author = request.user)
    context = {
        "pets" : pets
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addPet(request):
    form = PetForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        pet = form.save(commit=False)
        pet.author = request.user
        pet.save()
        messages.success(request,"Hayvan Başarılı Bir Şekilde Kaydedildi!")
        return redirect("pet:dashboard")

    context = {
        "form" : form
    }
    return render(request,"addpet.html",context)

@login_required(login_url="user:login")
def detail(request,id):
    pet = get_object_or_404(Pet,id=id)

    context = {
        "pet" : pet
    }

    return render(request,"detail.html",context)

@login_required(login_url="user:login")
def updatePet(request,id):

    pet = get_object_or_404(Pet,id=id)
    form = PetForm(request.POST or None, request.FILES or None,instance=pet)
    if form.is_valid():
        pet = form.save(commit=False)
        if request.user == pet.author or request.user.is_superuser:
            pet.save()
        else:
            messages.warning(request,"Seçilen Hayvanı Güncellemeye Yetkiniz Yok!")
            return redirect("pet:dashboard")
        messages.success(request,"Hayvan Başarılı Bir Şekilde Güncellendi")
        return redirect("pet:dashboard")

    context = {
        "form" : form
    }

    return render(request,"update.html",context)

@login_required(login_url="user:login")
def deletePet(request,id):
    pet = get_object_or_404(Pet,id=id)
    if request.user == pet.author.username or request.user.is_superuser:
        pet.delete()
    else:
        messages.warning(request,"Seçilen Hayvanı Silmeye Yetkiniz Yok!")
        return redirect("pet:dashboard")

    messages.success(request,"Kayıt Başarılı Bir Şekilde Silindi")   

    return redirect("pet:dashboard")     