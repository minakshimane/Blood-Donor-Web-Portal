from django.shortcuts import render,redirect
from BloodDonor.forms import RegisterForm,AdminForm
from BloodDonor.models import Donor,Admin,Organisation,Inbox
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.views.decorators.cache import cache_control


def showIndex(request):
    try:
        if request.session['dnr']:
            uname=request.session['dnr']
            return render(request,"index.html",{"name":uname})

    except:
        uname = request.GET.get("un")
        return render(request,"index.html",{"name":uname})



@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminlogin(request):
    uname=request.GET.get('un')
    try:
        if request.session['admin']:
            return render(request,"admin.html")
    except:

            return render(request,"adminlogin.html",{"name":uname})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def onlogin(request):
    unm = request.POST.get("admin")
    passw = request.POST.get("password")

    qs=Admin.objects.filter(username=unm,password=passw)
    if not qs:
            return render(request, "adminlogin.html", {"message": "Invalid User Or Password"})
    else:
            request.session['admin']=unm
            return render(request, "admin.html", {"message": "Welcome"})

def adminhome(request):
    return render(request,"admin.html")



def logout(request):
    del request.session['admin']

    return redirect('main')

def logoutd(request):
    del request.session['dnr']

    return redirect('main')


def showRegister(request):
    rf = RegisterForm()
    return render(request, "register.html", {"form": rf})

def savedonar(request):
    na = request.POST.get("name")
    unm = request.POST.get("username")
    upass = request.POST.get("password")
    gender = request.POST.get("gender")
    email = request.POST.get("email")
    contact = request.POST.get("contact")
    bgroup = request.POST.get("bloodgroup")
    cntry = request.POST.get("country")
    state = request.POST.get("state")
    city = request.POST.get("city")
    age = request.POST.get("age")
    weight = request.POST.get("weight")
    lddate = request.POST.get("ldd")

    rf = RegisterForm(request.POST)
    if rf.is_valid():
        Donor(name=na,username=unm,password=upass,gender=gender,email=email,contact=contact,bloodgroup=bgroup,country=cntry,state=state,city=city,age=age,weight=weight,ldd=lddate).save()
        messages.success(request, "Successfully Registered")
        return redirect('register')
    else:
        return render(request, "register.html", {"form": rf})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def organisation(request):
    try:
        if request.session['admin']:
            return render(request, "organisationReg.html")
    except:
        return redirect('main')



def saveOrganizationDetails(request):
    orgid=request.POST.get("orgid")
    orgname = request.POST.get("orgname")
    password = request.POST.get("password")
    type = request.POST.get("type")
    state = request.POST.get("state")
    city = request.POST.get("city")
    address=request.POST.get("address")
    cno = request.POST.get("contact")
    qs=Organisation.objects.filter(Orgid=orgid)
    if not qs:
        Organisation(Orgid=orgid,orgname=orgname, password=password, orgtype=type, state=state, city=city,address=address,contact=cno).save()
        return render(request, "organisationReg.html", {"message": "Organization Details Saved"})
    else:
        return render(request,"organisationReg.html",{"msg":"Org Id is already exist"})
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def profileView(request):
    try:
       if request.session['admin']:
           return render(request,"profile.html")
    except:
        return redirect('main')
def profilesViewOfDonor(request):
    qs = Donor.objects.all()
    return render(request, "donorprofile.html", {"data": qs})
def profilesViewOfOrg(request):
    qs = Organisation.objects.all()
    return render(request, "orgProfile.html", {"data": qs})





#donor login

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def donar(request):
    uname = request.GET.get("un")
    try:
        if request.session['dnr']:

            return render(request,'donarlog.html',{"name":uname})
    except:
        return render(request,"donar.html")

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def donarlog(request):

    uname = request.GET.get("un")
    return render(request, "donarlog.html", {"name": uname})


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def ondonarlogin(request):

    try:
        uname = request.POST.get("user")
        upass = request.POST.get("password")
        Donor.objects.get(username=uname, password=upass)
        request.session['dnr'] = uname
        return render(request, "donarlog.html", {"name": uname})
    except:
        messages.error(request, "Invalid User")
        return render(request, "donar.html", {"message": "Invalid User Or Password"})

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def donor_profile(request):

    try:
        uname = request.GET.get("un")

        stu = Donor.objects.get(username=uname)
        if request.session['dnr']:


            return render(request, "donar_profile.html", {"name": uname, "data": stu})
    except:
        return redirect('main')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def donar_update(request):


    try:
        uname = request.GET.get("un")
        stu = Donor.objects.get(username=uname)
        if request.session['dnr']:

            return render(request, "donor_update.html", {"name": uname, "data": stu})

    except:
        return redirect('main')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def update_donor(request):

    n=request.POST.get("u1")
    a=request.POST.get("u2")
    c=request.POST.get("u3")
    g=request.POST.get("u4")
    uname=request.POST.get("un")
    try:
        if request.session['dnr']:

            Donor.objects.filter(username=uname).update(name=n,age=a,contact=c,gender=g)
            stu=Donor.objects.get(username=uname)
            return render(request,"donar_profile.html",{"data":stu,"name":uname})
    except:
        return redirect('main')


















def leftdonar(request):
    uname=request.GET.get('un')
    return render(request, "aboutDonors.html",{"name":uname})
def leftdonarnext(request):
    st=request.POST.get("state")

    if st=="Maharashtra":
        str="Kolhapur"
        str1="Nashik"
        str3="Mumbai"
        return render(request, "aboutDonorsNext.html", {"data": str,"data1":str1,"data2":str3})
    elif st=="Andhrapradesh":
        str0 = "Vijaywada"
        str2 = "Vishkapatnam"
        str4 = "Vellure"
        return render(request, "aboutDonorsNext.html", {"data": str0, "data1": str2, "data2": str4})
    elif st == "Telangana":
        str0 = "Hyderabad"
        str2 = "Sikndarabad"
        str4 = "Ameerpeth"
        return render(request, "aboutDonorsNext.html", {"data": str0, "data1": str2, "data2": str4})


    else:
        return render(request, "aboutDonorsNext.html", {"data": str})

def gly(request):
    return render(request,"gallery.html")
def onsecondnext(request):
    st=request.POST.get("bgroup")
    st1=request.POST.get("city")

    if st1=="Kolhapur" and st=="A+" or 'B+' or 'O+' :
        qs1 = Donor.objects.filter(bloodgroup=st,city=st1)
        if not qs1:
            return render(request,'aboutDonorsSecondNext.html',{'message':'no donor found for','error':st,'city':st1})


        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
   # elif st1=="Kolhapur" and st=="O+":
    #    qs1 = Donor.objects.filter(bloodgroup="O+", city="Kolhapur")

     #   return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
    #elif st1 == "Kolhapur" and st == "B+":
     #   qs1 = Donor.objects.filter(bloodgroup="B+", city="Kolhapur")

      #  return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
    elif st1 == "Nashik" and st == "B+" or 'A+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
    elif st1 == "Mumbai" and st == "A+" or 'B+' or "O+":
        qs1 = Donor.objects.filter(bloodgroup=st,city=st1)
        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})


    elif st1=="Vijaywada" and st=="A+" or 'B+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
    elif st1 == "Vishkapatnam" and st == "A+" or 'B+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
    elif st1 == "Vellure" and st == "A+" or 'B+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})

    elif st1=="Hyderabad" and st=="B+" or 'A+' or 'B+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})

    elif st1=="Sikndarabad" and st=="B+" or 'A+' or 'B+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})

    elif st1=="Ameerpeth" and st=="B+" or 'A+' or 'B+' or 'O+':
        qs1 = Donor.objects.filter(bloodgroup=st, city=st1)

        return render(request, "aboutDonorsSecondNext.html", {"data": qs1})
    else:
        return render(request,"aboutDonorsSecondNext.html",{"message":"no donor found"})




def showdonor(request):
    uname = request.GET.get("un")
    stu = Donor.objects.get(username=uname)

    return render(request,"showdonor.html",{"data":stu})


def leftBloodBank(request):
    uname=request.GET.get('un')
    return render(request, "aboutBloodBank.html",{"name":uname})

def leftBloodBankNext(request):
    st = request.POST.get("state")

    if st == "Maharashtra":
        str = "Kolhapur"
        str1 = "Nashik"
        str3 = "Mumbai"
        return render(request, "aboutonBankNext.html", {"data": str, "data1": str1, "data2": str3})
    elif st == "Andhrapradesh":
        str0 = "Vijaywada"
        str2 = "Vishkapatnam"
        str4 = "Vellure"
        return render(request, "aboutonBankNext.html", {"data": str0, "data1": str2, "data2": str4})
    elif st == "Telangana":
        str0 = "Hyderabad"
        str2 = "Sikndarabad"
        str4 = "Warangal"
        return render(request, "aboutonBankNext.html", {"data": str0, "data1": str2, "data2": str4})
    else:
        return render(request, "aboutBloodBank.html", {"message": "There is no any blood Bank"})


def leftBloodBanksecondNext(request):

   # st1 = request.POST.get("city")


    #if st1 == "Kolhapur" :
     #   qs1 = Organisation.objects.filter(city="Kolhapur")

      #  return render(request, "aboutonSecondBankNext.html", {"data": qs1})
    #elif st1 == "Vijaywada":
     #   qs1 = Organisation.objects.filter(city="Vijaywada")

      #  return render(request, "aboutonSecondBankNext.html", {"data": qs1})
    #elif st1 == "Hyderabad" :
     #   qs1 = Organisation.objects.filter(city="Hyderabad")

      #  return render(request, "aboutonSecondBankNext.html", {"data": qs1})

    #else:
     #   return
   #st1 = request.POST.get("city")
   #res=Organisation.objects.get(city=st1)

   #if res=="Vijaywada":

   st1=request.POST.get("city")
   if st1=="Vijaywada":

       qs=Organisation.objects.filter(city="Vijaywada",state="Andhrapradesh",orgtype="Blood Bank")
       if not qs:
           return render(request,'aboutonSecondBankNext.html',{'message':"No Blood Bank Found","error":st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
   elif st1=="Kolhapur":
       qs=Organisation.objects.filter(city="Kolhapur",state="Maharashtra",orgtype="Blood Bank")
       if not qs:
           return render(request,'aboutonSecondBankNext.html',{'message':"No Blood Bank Found","error":st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
       #return render(request,"aboutonSecondBankNext.html",{"data":qs})
   elif st1 == "Nashik":
       qs = Organisation.objects.filter(city="Nashik", state="Maharashtra",orgtype="Blood Bank")
       if not qs:
           return render(request, 'aboutonSecondBankNext.html', {'message': "No Blood Bank Found", "error": st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
   elif st1 == "Mumbai":
       qs = Organisation.objects.filter(city=st1, state="Maharashtra", orgtype="Blood Bank")
       if not qs:
           return render(request, 'aboutonSecondBankNext.html', {'message': "No Blood Bank Found", "error": st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
   elif st1=="Hyderabad":
       qs=Organisation.objects.filter(city='Hyderabad',state="Telangana",orgtype="Blood Bank")
       if not qs:
           return render(request,'aboutonSecondBankNext.html',{'message':"No Blood Bank Found","error":st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
     #  return render(request, "aboutonSecondBankNext.html", {"data": qs})
   elif st1 == "Sikndarabad":
       qs = Organisation.objects.filter(city='Sikndarabad', state="Telangana", orgtype="Blood Bank")
       if not qs:
           return render(request, 'aboutonSecondBankNext.html', {'message': "No Blood Bank Found","error":st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
   elif st1 == "Vishkapatnam":
       qs = Organisation.objects.filter(city=st1, state="Andhrapradesh", orgtype="Blood Bank")
       if not qs:
           return render(request,'aboutonSecondBankNext.html',{'message':"No Blood Bank Found","error":st1})
       else:
           return render(request, "aboutonSecondBankNext.html", {"data": qs})
       #return render(request, "aboutonSecondBankNext.html", {"data": qs})
   else:
       return render(request,"aboutonSecondBankNext.html",{"message":"No Blood Bank Found","error":st1})

def other(request):
     qs=Organisation.objects.filter(orgtype="Blood Bank")
     return render(request,"other.html",{"data":qs})

def org(request):
    return render(request, "organizationlogin.html")

def orgLogin(request):


    ad = request.POST.get("admin")
    apass = request.POST.get("password")
    qs = Organisation.objects.filter(orgname=ad, password=apass)
    if not qs:
        return render(request, "organizationlogin.html", {"message": "Invalid User Or Password"})
    else:
        return render(request, "orgOnLogin.html", {"message": "Welcome"})


def faqs(request):
    uname=request.GET.get('un')
    return render(request,"faqs.html",{"name":uname})
def inboxTo(request):
    us =request.POST.get("user")
    em=request.POST.get("email")
    cn=request.POST.get('contact')
    msg = request.POST.get("message")
    Inbox(username=us,email=em,contact=cn,message=msg).save()
    return render(request,"faqs.html",{"message":"Message sent"})


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def inbox(request):
    try:
        if request.session['admin']:

             qs = Inbox.objects.all()
             return render(request, "inbox.html", {"data": qs})
    except:
        return redirect('main')

def lefthospital(request):
    uname=request.GET.get('un')
    return render(request,"aboutHospital.html",{"name":uname})

def leftHospitalNext(request):
    st = request.POST.get("state")

    if st == "Maharashtra":
        str = "Kolhapur"
        str1 = "Nahik"
        str3 = "Mumbai"
        return render(request, "aboutonHospitalNext.html", {"data": str, "data1": str1, "data2": str3})
    elif st == "Andhrapradesh":
        str0 = "Vijaywada"
        str2 = "Vishkapatnam"
        str4 = "Vellure"
        return render(request, "aboutonHospitalNext.html", {"data": str0, "data1": str2, "data2": str4})
    elif st == "Telangana":
        str0 = "Hyderabad"
        str2 = "Sikndarabad"
        str4 = "Warangal"
        return render(request, "aboutonHospitalNext.html", {"data": str0, "data1": str2, "data2": str4})
    else:
        return render(request, "aboutonHospitalNext.html", {"message": "There is no any blood Bank"})


def leftHospitalSecondNext(request):
    st1 = request.POST.get("city")
    if st1 == "Vijaywada":
        qs = Organisation.objects.filter(city="Vijaywada", state="Andhrapradesh", orgtype="Hospital")
        if not qs:
            return render(request, 'aboutonSecondHospitalNext.html', {'message': "No Hospital Found",'error':st1})
        else:
            return render(request, "aboutonSecondHospitalNext.html", {"data": qs})
    elif st1 == "Vishkapatnam":
        qs = Organisation.objects.filter(city=st1, state="Andhrapradesh", orgtype="Hospital")
        if not qs:
            return render(request, 'aboutonSecondHospitalNext.html', {'message': "No Hospital Found", 'error': st1})
        else:
            return render(request, "aboutonSecondHospitalNext.html", {"data": qs})
    elif st1 == "Kolhapur":
        qs = Organisation.objects.filter(city="Kolhapur", state="Maharashtra", orgtype="Hospital")
        if not qs:
            return render(request, 'aboutonSecondHospitalNext.html', {'message': "No Hospital Found",'error':st1})
        else:
            return render(request, "aboutonSecondHospitalNext.html", {"data": qs})
    elif st1 == "Nashik":
        qs = Organisation.objects.filter(city=st1, state="Maharashtra", orgtype="Hospital")
        if not qs:
            return render(request, 'aboutonSecondHospitalNext.html', {'message': "No Hospital Found", 'error': st1})
        else:
            return render(request, "aboutonSecondHospitalNext.html", {"data": qs})

    elif st1 == "Hyderabad":
        qs = Organisation.objects.filter(city='Hyderabad', state="Telangana",orgtype="Hospital")
        if not qs:
            return render(request, 'aboutonSecondHospitalNext.html', {'message': "No Hospital Found",'error':st1})
        else:
            return render(request, "aboutonSecondHospitalNext.html", {"data": qs})
    elif st1 == "Sikndarabad":
        qs = Organisation.objects.filter(city=st1, state="Telangana", orgtype="Hospital")
        if not qs:
            return render(request, 'aboutonSecondHospitalNext.html', {'message': "No Hospital Found",'error':st1})
        else:
            return render(request, "aboutonSecondHospitalNext.html", {"data": qs})
    else:
        return render(request, "aboutonSecondHospitalNext.html",{"message":"No Hospital Found In",'error':st1})


def benefits(request):
    uname=request.GET.get('un')
    return render(request,"benefits.html",{"name":uname})

def important(request):
    uname = request.GET.get('un')
    return render(request,"important.html",{"name":uname})

def whbenefits(request):
    uname = request.GET.get('un')
    return render(request,"whbenefits.html",{"name":uname})

def dashboard(request):

    m=Donor.objects.filter(bloodgroup='A+').count()
    print(m)
    n=Donor.objects.filter(bloodgroup='B').count()
    print(n)
    s=Donor.objects.filter(bloodgroup='A').count()
    qs=Donor.objects.all()
    t=Donor.objects.all().count()
    o=Organisation.objects.all()
    mess=Inbox.objects.all().count()
    return render(request,'dashboard.html',{'data':m,'data1':n,'data2':s,'db':qs,'total':t,'org':o,'mess':mess})

