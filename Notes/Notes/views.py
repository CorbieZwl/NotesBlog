from django.http import HttpResponseRedirect




def redirect_None(request):
    return HttpResponseRedirect("/home/index.html")