from django.shortcuts import redirect, render
from .models import ChiefModel,RecordsManger,Manager
from .form import StaffForm,Bannerfo
from CustomerApp.models import CusDashboard
from .form import BeveragesForm
import os
from CustomerApp.models import BeveragesModel

# Create your views here.  M_dashboard.html ,manager/M_dashboard.html

def MangerLogin(request):
    if request.method=='POST':
        #  'UserId': ['ravi@1234'], 'Password': ['1234']}>
        if 'Login' in request.POST:
            user=(request.POST['UserId'])
            password=(request.POST['Password'])
            try:
                obj=Manager.objects.get(pk=user)
                if obj:
                    if obj.Password == password:
                        request.session['ManagerUserid']=user
                        print(obj)
                        return redirect("Ma_Dashboard")
                    else:
                        print("User Id was Correct but Password is Wrong")
            except:
                return redirect("MangerLogin")
    return render(request,"login_form/loginManger.html")

def MangerLogOut(request):
    try:
        request.session.flush()
    except:
        pass
    return redirect("MangerLogin")


def ManagerDashboard(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")
    return render(request,"manager/M_dashboard.html")
def ManagerChiefList(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        if 'view' in request.POST:
            p=request.POST['id']
            obj=ChiefModel.objects.filter(id=p)
            if obj:
                obj=obj.values('id','ChiefName','C_Post','Chief_Number','Chief_Experiance','Cheif_AdharCard','UserId','Password')                
                obj=obj[0]
                obj=obj.items()
            return render(request,"manager/Chief_list.html",{'view':obj})
        elif 'update' in request.POST:
            id=request.POST['id']
            name=request.POST['ChiefName']
            post=request.POST['C_Post']
            phone=request.POST['Chief_Number']
            exper=request.POST['Chief_Experiance']
            adhar=request.POST['Cheif_AdharCard']
            user=request.POST['UserId']
            password=request.POST['Password']
            s=ChiefModel(id=id,ChiefName=name,Chief_Experiance=exper,C_Post=post,Cheif_AdharCard=adhar,Chief_Number=phone,UserId=user,Password=password)
            s.save()
            return redirect("ManagerChiefList")
        else:
            id=request.POST['id']
            pk=ChiefModel.objects.get(pk=id)
            pk.delete()
            return redirect("ManagerChiefList")
            
    obj=ChiefModel.objects.all()
    if obj:
        obj=obj.values('id','ChiefName','Chief_Experiance','C_Post')
    TableColumn=['ID','Chief Name','Experiance','Post']
    return render(request,"manager/Chief_list.html",{'table':{'column':TableColumn,'data':obj,'header':'Staff List'}})



#form section
def StaffAdd(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")


    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=StaffForm(request.POST)
            if fm.is_valid():
                fm.save()
                return redirect("ManagerChiefList")
    form=StaffForm()
    return render(request,"manager/Form.html",{'form':form,'header':' Staff Form 😉'})




#banner section
def Banner(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")


    if request.method=='POST':
        if 'Delete' in request.POST:
            id=(request.POST['id'])
            obj=CusDashboard.objects.get(pk=id)
            if obj:
                obj.delete()
                return redirect("Banner")
    obj=CusDashboard.objects.filter(BannerOfdata='banner')
    if obj:
        obj=obj.values('id','blockname','BannerOfdata')
    TableColumn=['id','blockname','BannerOfdata']
    return render(request,"manager/table_list.html",{'table':{'column':TableColumn,'data':obj,'header':'Banner List'}})
def bannerform(request,i):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    pi=CusDashboard.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit'in request.POST:
            if request.FILES:
                t="ProjectData/Media/"+str(pi.BannerImage)
                obj=CusDashboard(id=i,BannerOfdata=request.POST['BannerOfdata'],blockname=request.POST['blockname'],BannerImage=request.FILES['BannerImage'])
                obj.save()
                try:
                    os.remove(t)
                except Exception as x :
                    print("no deleted" ,x,t)
                return redirect("Banner")
                
            else:
                return redirect("Banner")
    
    obj=Bannerfo(instance=pi)
    return render(request,"manager/Form.html",{'form':obj,'header':' Banner Form 😉'})

#food coat
#Starter,Main_CourceModel,RiceChapati,Chinese_Snacks,SweetCornerModel,BeveragesModel
def MainMenuItems(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    return render(request,"manager/FoodcoatTable.html")
def beveragesIistAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=="POST":
        if 'Delete' in request.POST:
            obj=BeveragesModel.objects.get(pk=request.POST['id'])
            obj.delete()
            return redirect("beveragesIistAdmin")
        elif 'view'in request.POST:
            return redirect("BeveragesFormUpdateAdmin",i=request.POST['id'])
        elif 'AddItems' in request.POST:
            return redirect("BeveragesFormAdmin")
    obj=BeveragesModel.objects.all()
    obj=obj.values('id','DrinkName','DrinkType','DrinkCost')
    table=['id','DrinkName','DrinkType','DrinkCost']
    return render(request,"manager/MainMenuList.html",{'table':{'column':table,'data':obj,'header':'Beverages List','btn':'Add Beverages'}})    
def BeveragesFormAdmin(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    if request.method=='POST':
        fm=BeveragesForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect("beveragesIistAdmin")

    form=BeveragesForm()
    return render(request,"manager/Form.html",{'form':form,'header':' Banner Form 😉'})


def BeveragesFormUpdateAdmin(request,i):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    pk=BeveragesModel.objects.get(pk=i)
    if request.method=='POST':
        if 'Submit' in request.POST:
            fm=BeveragesForm(request.POST,request.FILES,instance=pk)
            if fm.is_valid():
                if request.FILES:
                    try:
                        fm.save()
                    except Exception as x:
                        print("not deleted",x)
                else:
                    fm.save()
                return redirect("beveragesIistAdmin")              
    form=BeveragesForm(instance=pk)
    return render(request,"manager/Form.html",{'form':form,'header':' Banner Form 😉'})


#Profile
def ProfileManger(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    return render(request,"manager/profile.html")


#Records
def RecordsManager(request):
    if 'ManagerUserid' not in request.session:
        return redirect("MangerLogin")

    obj=RecordsManger.objects.all()
    if obj:
        obj=obj.values('id','userid','TotalCost')
        TotalSale=0
        totalCustomer=0
        totalstaff=len(ChiefModel.objects.all())
        for i in obj:
            TotalSale=TotalSale + (float(i['TotalCost']))
            totalCustomer+=1
    column=['id','  Customer Id','₹ Amount']
    return render(request,"manager/Records.html",{'table':{'column':column,'data':obj,'TotalSale':TotalSale,'totalCustomer':totalCustomer,'totalstaff':totalstaff}})