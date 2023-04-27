from django.shortcuts import render

# Create your views here.
def builtin_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'never give up','dt':dt,'m':2}
    

    return render(request,'builtin_filter.html',d)