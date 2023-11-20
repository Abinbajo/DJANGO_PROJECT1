from django.shortcuts import render

# Create your views here.
def forloop(request):
    dict={'name':"abin"}
    return render(request,"forloop.html",context=dict)