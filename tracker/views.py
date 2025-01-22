from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from tracker.models import ReadEntry
from tracker.forms import ReadEntryForm
# Create your views here.

class ReadCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance = ReadEntryForm()
        return render(request,'read_create.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        form_data = request.POST
        form_instance = ReadEntryForm(form_data,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("read-list")
        return render(request,'read_create.html',{"form":form_instance})
class ReadListView(View):
    def get(self,request,*args,**kwargs):
        qs = ReadEntry.objects.all()
        return render(request,'read_list.html',{"data":qs})
class ReadDetailView(View):
    def get(self,request,*args,**kwargs):
        id= kwargs.get("pk")
        qs = ReadEntry.objects.get(id= id)
        return render(request,"read_detail.html",{"data":qs})
    


class ReadDeleteView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        ReadEntry.objects.get(id=id).delete()
        return redirect("read-list")
    

class ReadUpdateView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        read_obj = get_object_or_404(ReadEntry,id=id)
        form_instance = ReadEntryForm(instance=read_obj)
        return render(request,'read_update.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        read_obj = get_object_or_404(ReadEntry,id=id)
        form_instance = ReadEntryForm(request.POST, files=request.FILES, instance=read_obj)
        if form_instance.is_valid():
            form_instance.save()
            return redirect("read-list")
        return render(request,'read_update.html',{"form":form_instance})