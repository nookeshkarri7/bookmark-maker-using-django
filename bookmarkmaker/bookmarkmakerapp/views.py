from django.shortcuts import render
from . import forms
from bookmarkmakerapp.models import bookmarkMakertable
def bookmarkMaker(request):
    form=forms.bookmarkMakerForm()
    data=bookmarkMakertable.objects.all().order_by("-id")
    if request.method=="POST":
        form=forms.bookmarkMakerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form=forms.bookmarkMakerForm()
    return render(request, "index.html",{"form":form,"data":data})

def update_bookmark(request,id):
    eachdata=bookmarkMakertable.objects.get(id=id)
    return render(request,'update.html',{"form":eachdata})


