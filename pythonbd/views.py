from django.shortcuts import render

# Create your views here.

def index(request):
    data = ['Python','Django','ASP.NET']
    context ={'data': data}
    return render(request, 'pythonbd/index.html',context)


def about(request):
    data = ['50','Django','ASP.NET']
    context ={'data': data}
    return render(request, 'pythonbd/about.html',context)



def service(request):
    data = ['50','Django','ASP.NET']
    context ={'data': data}
    return render(request, 'pythonbd/service.html',context)