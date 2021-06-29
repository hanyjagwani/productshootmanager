from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login as dj_login
from django.contrib.auth import authenticate , logout
from django.contrib.sessions.models import Session
from .models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.
def start(request):
    return render(request, "login.html")

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.userprofile.user_type=='Host':
                dj_login(request,user)
                messages.success(request, 'login successful')
                request.session['is_logged']=True
                return redirect("/host1")
            else:
                dj_login(request,user)#correction
                request.session['is_logged']=True
                messages.success(request, 'login successful')
                user=request.user.id
                print('user'+str(user))
                request.session['user_id']=user
                return redirect('/index')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')
    else:
        return render( request, "login.html")
      
def index(request):
    if request.session.has_key('is_logged'):
        user_id = request.session['user_id']
        user=User.objects.get(id=user_id)
        obj=Design.objects.filter(user=user)
        dic={"i":obj}
        return render(request, "index.html",dic)
    return redirect("/")

def host1(request):
    if request.session.has_key('is_logged'):
        client=UserProfile.objects.filter(user_type="Client")
        o=Order.objects.all()
        
        return render(request,"host1.html", {"client": client,"o":o})    

def client(request,id):
    client=User.objects.filter(id=id)
    request.session["client_id"]=id
    return render(request,"nry.html", {"client": client})   

def register(request):
    return render(request,"reg.html")

def register_submit(request):
    if request.method=="POST":
        usern=request.POST["usern"]
        email=request.POST["email"]
        psw=request.POST["psw"]
        mob=request.POST["mob"]
        add=request.POST["add"]
        user=User.objects.create_user(usern,email,psw)
        user.save()
        user=User.objects.get(username=usern)
        user_client=UserProfile(user=user,user_type="Client",contact=mob,address=add)
        user_client.save()
        return redirect("/host1")
    return redirect("/")    

def client_form_submit(request):
    if request.method=="POST":
        item_name=request.POST["item_name"]
        item_price=request.POST["item_price"]
        images=request.FILES["images"]
        client_id=request.session["client_id"]
        user=User.objects.get(id=client_id)
        design=Design(user=user,description=item_name,price=item_price,img=images)
        design.save()
        return redirect("/host1")
    return HttpResponse("/")    

def handlelogout(request):
    del request.session['is_logged']
    del request.session['user_id']
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')

def hostlogout(request):
    del request.session['is_logged']
    logout(request)
    messages.success(request, " Successfully logged out")
    return redirect('/')

def checkout(request):
    if request.session.has_key('is_logged'):
        user_id = request.session['user_id']
        user=User.objects.get(id=user_id)
        if request.method=="POST":
            items_json = request.POST.get('itemsJson', '')
            bad_chars = ['{', '}', ' ']
            test_string = items_json            
            for i in bad_chars :
                test_string = test_string.replace(i, '')
            print ("Resultant list is : " + str(test_string))
            order = Order(user=user,items_json=test_string)
            order.save()
            thank = True
            id = order.order_id
            return render(request, 'checkout.html', {'thank':thank, 'id': id})
        return render(request, 'checkout.html')
    return HttpResponse("no")