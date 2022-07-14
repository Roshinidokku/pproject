from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product
# Create your views here.
class ProductInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class ProductInsert(View):
    def get(self,request):
        p_id=request.GET["t1"]
        p_name= request.GET["t2"]
        p_cost=request.GET["t3"]
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET['t5']
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        res=HttpResponse("product inserted successfully")
        return res