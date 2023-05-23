from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from myapp.forms import *
from myapp.models import *
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
import pdb
from django.db.models import Count
from django.shortcuts import render, redirect
from myapp.models import products
from django.contrib.auth.decorators import login_required
from cart.forms import CartAddProductForm
from orders.models import *
from django.contrib import messages
# Create your views here.

def mattressview(request):
    coll=category.objects.all()[0:3]
    return render(request,"mattress.html",{'coll':coll})
class aboutview(TemplateView):
    template_name="about.html"
class formview(TemplateView):
    template_name="form.html"  
class homeview(TemplateView):
    template_name="home.html"
class contactview(TemplateView):
    template_name="contact.html"  
class aboutview(TemplateView):
    template_name="about.html"
class servicesview(TemplateView):
    template_name="services.html"
class shippingview(TemplateView):
    template_name="shipping.html"
class Addblogsview(TemplateView):
    template_name="Addblogs.html"

    
def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)   
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent." )
            return redirect('/contact/')
    else:
            form=contactform()
            messages.error(request, "Error in sending message." )
    return render(request,"contact.html",{'form':form}) 
    
def blogview(request):
    blg=blogs.objects.filter(status='Approved').order_by('-id')
    return render(request,"blogs.html",{'blg':blg}) 

def blogsdetail(request,id):
    b=blogs.objects.get(id=id)
    return render(request,"blogsdetail.html",{'b':b}) 

def collection(request):
    c=category.objects.all()
    return render(request,"collection.html",{'c':c}) 

def Faqview(request):
    c=Faq.objects.all()
    return render(request,"Faq.html",{'c':c})

def productview(request,id):
    pro=products.objects.filter(categoryid_id=id).annotate(Count('likenow'))
    return render(request,"product.html",{'pro':pro}) 

def productdetail(request,id):
    c=products.objects.get(id=id)
    cart_product_form = CartAddProductForm()
    return render(request,"productdetail.html",{'c':c,'cart_product_form': cart_product_form}) 

def Myorderview(request):
    c=OrderItem.objects.select_related('order').filter(order__userid=request.user.id)
    return render(request,"Myorder.html",{'c':c})


def signupview(request):
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/blogs/')
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})

def dolike(request):
    #form=dolike()
    productid=request.GET['pid']
    userid=request.GET['uid']
    data={
        'is_taken': likenow.objects.filter(userid_id=userid,productid_id=productid).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'your like is already registered. you cannot do like again'
    else:
        form=likenow.objects.create(productid_id=productid,userid_id=userid)
        form.save()
        data['message']='your like is registred'
        return JsonResponse(data)
    return render(request,'product.html',{'form':form})

 
def insertemail(request):
    if request.method=='POST':
        form=subscribeform(request.POST)   
        if form.is_valid():
            form.save()
            return redirect('/mattress/')
    else:
            form=subscribeform()
    return render(request,"mattress.html",{'form':form}) 


def insertblogs(request):
    if request.method=='POST':
        form=Addblogsform(request.POST,request.FILES)   
        if form.is_valid():
            form.save()
            return redirect('/blogs/')
        else:
            form=Addblogsform()
    return render(request,"Addblogs.html",{'form':form}) 
