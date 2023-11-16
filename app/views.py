from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='jspiders gives better future trust me and study hard'
    d={'access':data,'location':'marathali'}
    return render(request,'data_render.html',context=d)