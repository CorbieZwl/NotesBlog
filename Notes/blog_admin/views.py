from django.shortcuts import render

# Create your views here.

def root_login(request):
    return render(request,'blog_admin/login.html')
