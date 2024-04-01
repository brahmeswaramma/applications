from django.shortcuts import render

# Create your views here.
def htmlpage(request):
    return render(request,'htmlpage.html')