from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from . forms import Registerform,Insertform
from . models import Records

# Create your views here.

def home(request):
    return render(request,'home.html')


#user_registration
def register(request):
    if(request.method=='GET'):
        form=Registerform()
        context={'form':form}
        return render(request,'register.html',context)
    if(request.method=='POST'):
        form=Registerform(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request,'your account created successfully!')
            return redirect('login')
        else:
            context={'form':form}
            return render(request,'register.html',context)

#login_user
def user_login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if(user is not None):
            login(request, user)
            messages.success(request,'you are successfuly logged in !')
            return redirect('dashboard')
        else:
            messages.error(request,'credentials did not match !')
            return redirect('login')
    return render(request,'login.html')

#user_logout
def user_logout(request):
    logout(request)
    messages.success(request,'you are successfully logged out !')
    return redirect('home')


#user_dashboard
@login_required
def dashboard(request):
    user = request.user
    records=user.records.all()
    count=records.count()
    context={
        'records':records,'user':user,'count':count
    }
    return render(request,'dashboard.html',context)


#insert_record

@login_required
def insert(request):
    if(request.method=='GET'):
        form=Insertform()
        context={'form':form}
        return render(request,'insert.html',context)
    if(request.method=='POST'):
        form=Insertform(request.POST)
        if(form.is_valid()):
            record=form.save(commit=False)
            #save the user with currentuser
            record.user = request.user
            record.save()
            messages.success(request,'Data inserted Sucessfully!')
            return redirect('dashboard')
        else:
            context={'form':form}
            return render(request,'insert.html',context)

#to get a single record
@login_required
def view(request,pk):
    record=Records.objects.get(id=pk)
    context={'record':record}
    return render(request,'view.html',context)

#update the record
@login_required
def update(request,pk):
    old_record=Records.objects.get(id=pk)
    if(request.method=='GET'):
        old_record=Records.objects.get(id=pk)
        form=Insertform(instance=old_record)
        context={'form':form,'old_record':old_record}
        return render(request,'update.html',context)
    if(request.method=='POST'):
        form=Insertform(request.POST,instance=old_record)
        if(form.is_valid()):
            form.save()
            messages.success(request,'data updated successfully!')
            return redirect('dashboard')
        else:
            context={
                'form':form
            }
            return render(request,'update.html',context)
        

#delete the record
@login_required
def delete(request,pk):
    record=Records.objects.get(id=pk)
    record.delete()
    messages.success(request,'Data deleted Successfully!')
    return redirect('dashboard')
