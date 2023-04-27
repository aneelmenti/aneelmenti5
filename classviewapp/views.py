from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class Input(View):
    def get(self,request):
        return render(request,'input.html')
class Add(View):
    def get(self,request):
        a=int(request.GET["t1"])
        b=int(request.GET["t2"])
        z=a+b
        res=HttpResponse("the sum is: "+str(z))
        return res

