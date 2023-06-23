from django.shortcuts import render
from django.http import HttpResponse
from MainApp.models import links,action,anime,horror,romance,downloadpage


# Create your views here.

def loginpage(request):
    data={
        'title':"Login"
    }
    return render (request,"loginpage.html")

def Signup(request):
    data={
        'title':"Signup"
    }
    return render (request,"Signuppage.html")


def Homepage(request):
    link=links.objects.all()
    actions=action.objects.all()
    animes=anime.objects.all()
    horrors=horror.objects.all()
    romances=romance.objects.all()
    data={
        'title':"Streamflix",
        'links':link,
        'actions':actions,
        'animes':animes,
        'horrors':horrors,
        'romances':romances
    }
    return render (request,"Homepage.html",data)

def feature(request):
    link=links.objects.all()
    data={
        'title':"Features",
        'links':link,
    }
    return render (request,"features.html",data)

def privacy(request):
    link=links.objects.all()
    data={
        'title':"Privacy Policy",
        'links':link,
    }
    return render (request,"privacy.html",data)

def aboutus(request):
    link=links.objects.all()
    data={
        'title':"Aboutus",
        'links':link,
    }
    return render (request,"aboutus.html",data)

def termsandservices(request):
    link=links.objects.all()
    data={
        'title':"Terms And Services",
        'links':link,
    }
    return render (request,"termsandservices.html",data)

def download(request):
    link=links.objects.all()
    downloaddata=downloadpage.objects.all().order_by('-id')
    data={
        'title':"Download Page",
        'links':link,
        'downloaddata':downloaddata,
    }
    return render (request,"downloadpage.html",data)

