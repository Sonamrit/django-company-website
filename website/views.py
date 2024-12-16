from django.shortcuts import render
from .models import *
from .contact_form import ContactForm

# Create your views here.
def index(request):
    data ={
        'aboutUs': Page.objects.get(page_section_name ='about-us'),
        'serviceData': Service.objects.order_by('-id')[:4],
        'blogData':Blog.objects.order_by('-id')[:3], 
    }
    return render(request,'index.html',data)

def about(request):
    data ={
        'aboutUs': Page.objects.get(page_section_name ='about-us'),
    }
    return render(request,'about.html',data)

def service_views(request):
    data={
        'serviceData' : Service.objects.all(),
    }
    return render(request,'service.html',data)



def service_details(request,slug):
    data={
        'serviceData' : Service.objects.get(slug=slug),
    }
    return render(request,'service-details.html',data)

def blog_views(request):
    data={
        'blogData' : Blog.objects.all(),
    }
    return render(request,'blog.html',data)



def blog_details(request,slug):
    data={
        'blogData' : Blog.objects.get(slug=slug),
    }
    return render(request,'blog-details.html',data)

def contact_view(request):
    if request.method == 'POST':
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            contactForm.save()
            return render(request,'contact.html',{'contactForm':ContactForm()})
        else:
            return render(request,'contact.html',{'contactForm':contactForm})
    else:
       data={
         'contactForm': ContactForm(),

    }
    return render(request,'contact.html',data)

