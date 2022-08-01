import os

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import *
from  django.contrib.auth import login,logout
from . models import EmployeeExperience,EmployeeDetail,EmployeeEducation
# Create your views here.
def index(request):
    return render(request,'index.html')

def registration(request,user_exist=None):
    error = ""
    user = request.user
    user = User.objects.filter(username=user)
    if request.method =='POST'and request.FILES:
        fn=request.POST['firstname']
        ln = request.POST['lastname']
        ec = request.POST['empcode']
        em = request.POST['email']
        pwd = request.POST['pwd']
        image = request.FILES['image']

        # user_exist = User.objects.filter(username=em)
        #
         # if user_exist:
         #     return HttpResponse("User Already Exist")
         #
         # else:
        try:
            user=User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
            EmployeeDetail.objects.create(user=user,empcode=ec,image=image)
            EmployeeEducation.objects.create(user=user)
            EmployeeExperience.objects.create(user=user)
            error="no"
            user.save()
        except:
            error="yes"

        # if user:
        #     return render(request,'emp_login.html',locals())


    return render(request,'registration.html',locals())



def emp_login(request):
    error = ""
    if request.method =='POST':
        u = request.POST.get('email')
        p = request.POST.get('password')
        user = authenticate(username=u,password=p)
        if user:
            login(request,user)
            error = "no"
            return render(request,'emp_home.html',locals())

        else:
            error="yes"
    return render(request,'emp_login.html',locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
        # return render(request,'emp_home.html')


def profile(request):
    error=""
    #compair current user

    user=request.user
    user = User.objects.filter(username=user)
    employee=EmployeeDetail.objects.filter(user=user)
    employee=EmployeeDetail()

    if request.method =='POST':
        fn = request.POST.get('firstname')
        ln = request.POST.get('lastname')
        ec = request.POST.get('empcode')
        designation = request.POST.get('designation')
        department= request.POST.get('department')
        contact= request.POST.get('contact')
        joiningdate = request.POST.get('joiningdate')
        gender = request.POST.get('gender')
        image = request.FILES.get('image')


        employee.first_name = fn
        employee.last_name = ln
        employee.empcode = ec
        employee.department = department
        employee.designation = designation
        employee.contact= contact
        employee.joiningdate =joiningdate
        employee.gender =gender
        employee.image=image


        if joiningdate:
            employee.joiningdate = joiningdate
            error = "no"
            return render(request, 'all_employee.html', locals())

    try:
        employee.save()
        employee.user.save()
        #local variable=error

    except:
        error = "yes"
        return render(request, 'profile.html', locals())



def admin_login(request):
    error = ""
    if request.method=='POST':
        u =request.POST.get('username')
        p = request.POST.get('password')
        user=authenticate(username=u,password=p)

        try:
            if user.is_staff:
                login(request,user)
                error = "yes"
                return render(request, 'admin_login.html', locals())
            else:
                error="yes"
        except:
            error = "no"
            return redirect('all_employee')
        return render(request,'all_employee.html',locals())


def my_experience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    experience=EmployeeExperience.objects.filter(user=user)
    return render(request,'my_experience.html',locals())



def edit_myexperience(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    user = User.objects.get(username=user)
    error=""
    experience=EmployeeExperience.objects.filter(user=user)
    if request.method=='POST':
        company1name=request.patch('company1name')
        company1desig = request.patch('company1desig')
        company1salary = request.patch('company1salary')
        company1duration = request.patch('company1duration')

        company2name = request.patch('company2name')
        company2desig = request.patch('company2desig')
        company2salary = request.patch('company2salary')
        company2duration = request.patch('company2duration')

        company3name = request.patch('company3name')
        company3desig = request.patch('company3desig')
        company3salary = request.patch('company3salary')
        company3duration = request.patch('company3duration')


        experience.company1name = company1name
        experience.company1desig = company1desig
        experience.company1salary = company1salary
        experience.company1duration  = company1duration

        experience.company2name = company2name
        experience.company2esig = company2desig
        experience.company2salary = company2salary
        experience.company2duration = company2duration

        experience.company3name = company3name
        experience.company3desig = company3desig
        experience.company3salary = company3salary
        experience.company3duration = company3duration
        try:
            experience.save()
            error="no"
            return render(request, 'all_employee.html', locals())

        except:
            error="Yes"
    return render(request,'edit_myexperience.html',locals())

def my_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user
    user = User.objects.get(username=user)
    education=EmployeeEducation.objects.filter(user=user)
    return render(request,'my_education.html',locals())

def edit_myeducation(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user

    error=""
    #compair current user
    user=request.user
    education=EmployeeEducation.objects.filter(user=user)

    if request.method=='POST':

        courcepg=request.POST.patch('courcepg')
        schoolclgpg= request.POST.patch('schoolclgpg')
        yearofpassingpg= request.POST.patch('yearofpassingpg')
        percentagepg = request.POST.patch('percentagepg')

        courcegra = request.POST.patch('courcegra')
        schoolclggra = request.POST.patch('schoolclggra')
        yearofpassinggra = request.POST.patch('yearofpassinggra')
        percentagegra = request.POST.patch('percentagegra')

        courcessc = request.POST.patch('courcessc')
        schoolclgssc = request.POST.patch('schoolclgssc')
        yearofpassingssc = request.POST.patch('yearofpassingssc')
        percentagessc = request.POST.patch('percentagessc')

        courcehsc = request.POST.patch('courcehsc')
        schoolclghsc = request.POST.patch('schoolclghsc')
        yearofpassinghsc = request.POST.patch('yearofpassinghsc')
        percentagephsc= request.POST.patch('percentagehsc')



        education.courcepg = courcepg
        education.schoolclgpg = schoolclgpg
        education.yearofpassingpg = yearofpassingpg
        education.percentagepg  = percentagepg

        education.courcegra = courcegra
        education.schoolclggra = schoolclggra
        education.yearofpassinggra = yearofpassinggra
        education.percentagegra = percentagegra

        education.courcessc = courcessc
        education.schoolclgssc = schoolclgssc
        education.yearofpassingssc = yearofpassingssc
        education.percentagepssc = percentagessc


        education.courcehsc = courcehsc
        education.schoolclghsc = schoolclghsc
        education.yearofpassinghsc = yearofpassinghsc
        education.percentagephsc = percentagephsc

        try:
            education.save()
            error="no"
            return render(request, 'all_employee.html', locals())
        except:
            error="Yes"
    return render(request,'edit_myeducation.html',locals())



def change_password(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')

    error = ""
    #compair current user
    user=request.user
    if request.method=='POST':
        c=request.POST.get('currentpassword')
        n=request.POST.get('newpassword')

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error="not"

        except:
            error="Yes"
    return render(request,'change_password.html',locals())


def change_adminpassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    error = ""
    #compair current user
    user=request.user
    if request.method=='POST':
        c=request.POST.get('currentpassword')
        n=request.POST.get('newpassword')

        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
            else:
                error="not"

        except:
            error="Yes"
    return render(request,'change_adminpassword.html',locals())

'''def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request,'admin_home.html')'''


def all_employee(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    employee=EmployeeDetail.objects.all()
    for i in employee:
        print(i.image)
    context={
        'employee':employee,
    }
    print('context',context)
    return render(request,'all_employee.html',locals())


def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error=""
    #compair current user
    user=request.user
    employee=EmployeeDetail.objects.filter(user=user)
    employee=EmployeeDetail()
    if request.method =='POST':
        # if len(request.FILES)!=0:
        #     if len(employee.image)>=0:
        #         os.remove(employee.image.path)
        #     employee.image=request.FILES.get('image')
        # EmployeeDetail=request.POST['employee']
        fn=request.POST.patch('firstname')
        ln = request.POST.patch('lastname')
        ec = request.POST.patch('empcode')
        designation = request.POST.patch('designation')
        department= request.POST.patch('department')
        contact= request.POST.patch('contact')
        jdate = request.POST.patch('jdate')
        gender = request.POST.patch('gender')
        image = request.FILES.patch('image',None)
        # print(image,'image')
        # employee.objects.filter(id=pid)
        image = EmployeeDetail.objects.filter(image=image)
        return redirect('all_employee')

        employee.user.first_name = fn
        employee.user.last_name = ln
        employee.empcode = ec
        user.department = department
        user.designation = designation
        user.contact= contact
        user.gender =gender
        user.image=image

        user.image.save()

        if jdate:
            employee.joiningdate=jdate
        try:
            employee.save()
            user.save()
        #local variable=error
            error="no"
        except:
            error="Yes"
    return render(request,'edit_profile.html',locals())




def Logout(request):
    logout(request)#session variable destroy
    return redirect('index')

def delete_employee(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    user=User.objects.get(id=pid)
    user.delete()
    return redirect('all_employee')
