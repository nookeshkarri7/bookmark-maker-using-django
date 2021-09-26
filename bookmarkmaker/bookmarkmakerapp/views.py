from django.shortcuts import render,redirect
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
    if request.method=="POST":
        form=forms.bookmarkMakerForm(request.POST,instance=eachdata)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request,'update.html',{"form":eachdata})


def delete_bookmark(request,id):
    eachdata=bookmarkMakertable.objects.get(id=id)
    eachdata.delete()
    return redirect("/")
    


