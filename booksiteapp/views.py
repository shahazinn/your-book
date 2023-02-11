from django.shortcuts import render,redirect
from bookapp.models import bitdb,prodb
from booksiteapp.models import CustomerDetailes,adcontact,itemcart
from django.contrib import messages

# Create your views here.
def index4(request):
    data=bitdb.objects.all()
    return render(request,"index1.html",{'data':data})

def contactpage(request):
    data = bitdb.objects.all()
    return render(request,"contact.html",{'data':data})

def aboutpage(request):
    data = bitdb.objects.all()
    return render(request,"about.html",{'data':data})
def blogpage(request):
    data = bitdb.objects.all()
    return render(request,"blog.html",{'data':data})
def product3(request):
    data=prodb.objects.all()
    return render(request,"product.html",{'data':data})
def discategory(request,itemcatg):
    data=bitdb.objects.all()

    print("===itemcatg===",itemcatg)
    catg=itemcatg.upper()

    products=prodb.objects.filter(category=itemcatg)
    context={
        'products':products,
        'catg':catg,
        'data':data,


    }
    return render(request,"categorydisplay.html",context)

def prodetails(request,dataid):
    datas=prodb.objects.get(id=dataid)
    data=bitdb.objects.all()
    return render(request,"productdetails.html",{'dat':datas,'data':data})

def logregpage(request):
    data=bitdb.objects.all()
    return render(request,"logreg.html",{'data':data})
def regdata(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pass1')
        confirm_password=request.POST.get('pass2')
        if password==confirm_password:
            obj=CustomerDetailes(username=username,email=email,password=password,confirm_password=confirm_password)
            obj.save()
            return redirect(logregpage)
        else:
            messages.warning(request, "password and confirm password does not match")
    return render(request,'logreg.html')

def customerlogin(request):
    if request.method=="POST":
        username_r=request.POST.get('username')
        password_r=request.POST.get('password')
        if CustomerDetailes.objects.filter(username=username_r,password=password_r).exists():
            data=CustomerDetailes.objects.filter(username=username_r,password=password_r).values('email','id').first()
            request.session['username']=username_r
            request.session['password']=password_r


            return redirect(index4)
        else:
            messages.warning(request, "sorry invalid user")
    return render(request,'logreg.html')


def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(index4)

def adcontactsave(request):
    if request.method=="POST":
        na=request.POST.get('name')
        em=request.POST.get('email')
        ms=request.POST.get('message')
        obj=adcontact(name=na,email=em,message=ms)
        obj.save()
        return redirect(contactpage)
def cartpage(request):
    data=itemcart.objects.all()
    return render(request,"cart.html",{'data':data})

def cartsave(request):
    if request.method=="POST":
        pro=request.POST.get('product')
        qua=request.POST.get('qty')
        tpri=request.POST.get('totalprice')
        obj=itemcart(product=pro,quantity=qua,totalprice=tpri)
        obj.save()
        return redirect(cartpage)
def deletecart(request,dataid):
    data=itemcart.objects.filter(id=dataid)
    data.delete()
    return redirect(cartpage)
