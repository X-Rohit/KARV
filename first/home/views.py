from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse,redirect
from home.models import Secret,register,Transaction
from django.contrib import messages
from nsetools import Nse
from django.db import connection
import re
 
# Make a regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
 

 
    # pass the regular expression
    # and the string into the fullmatch() method
    
 




# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")

def second(request):
    if request.session.has_key('uid'):
      if request.method == "POST" :

        username= request.POST.get('username')
        email=request.POST.get('Email')
        sector=request.POST.get('sector')
        symbol=request.POST.get('symbol')
        price=request.POST.get('price')
        peratio=request.POST.get('peratio')
        weekup=request.POST.get('52weekup')
        weekdown=request.POST.get('52weekdown')

        if(re.fullmatch(regex, email)):
            print("Valid Email")
            secret=Secret(username=username, email=email, sector=sector, symbol=symbol, price=price, peratio=peratio, weekup=weekup, weekdown=weekdown)
            secret.save()
            messages.success(request, 'Your status is now stored.')
        else:
            messages.warning(request, 'Invalid Email.')
       
         

       

        return render(request,'second.html')
      return render(request,'second.html')
    else:
       return redirect("/index") 
    

def signup(request):
    if request.method == "POST" :
        uname = request.POST.get('uname')
        email= request.POST.get('email')
        password = request.POST.get('password')

        if(re.fullmatch(regex, email)):
            print("Valid Email")
            signup = register(username=uname, email=email, password=password, coins=10000)
            signup.save()

    return render(request,'signup.html')





def login(request):
    if request.method == "POST" :
        uname = str(request.POST.get('uname'))
        password = request.POST.get('password')
        
# to acess the data from database
        user = register.objects.raw('SELECT * FROM home_register WHERE username= %s',[uname])
     
        for u in user :
            print(u.username)
            print(u.password)
            if u.username==uname and u.password==password :
                request.session['uid']=str(request.POST.get('uname'))
                print('you are user')
                return redirect("/second") 
            else :
             messages.warning(request, 'You dont have a accout, signup first.')
             return render(request,'login.html')
     
    return render(request,'login.html')       
    






# ###########################################################################3
nse = Nse()
 
x="rohan"
a="sbin"
b=3
totalcoins=0
total=0

def calculate(request):
    
      if 'uid' in request.session:              #to get data from session 
          x=request.session['uid']
          print(x)
        


      if request.method == "POST" :
         name=request.POST.get('ticker')
         a=name
         stocks=request.POST.get('stocks')
         b=int(stocks)
         print(x,a,b)


         quote = nse.get_quote(a)
        #  companyname=quote['companyName']
        # #  price=int(quote['buyPrice1'])

        #  print (companyname)
         return redirect("/dashboard") 

        

    #   if (price==None):
    #       messages.warning(request, 'Sorry market is off try again tommorow morning .')
    #       return redirect("/dashboard") 
    #   else:
    #     total=price*b
    #     print(companyname, price,total)




    #   coindata=register.objects.raw('SELECT * FROM home_register WHERE username= %s', [x])
    #   for c in coindata:
    #       print(c.coins)
    #       totalcoins=int(c.coins)
    #   if (totalcoins>= total):
    #       savedata=Transaction(username=x,ticker=name,TotalShare=b,TotalAmount=total,status="purchase")
    #       savedata.save()
    #       newcoin=totalcoins-total
        
    #       obj=register.objects.get(username=x)
    #       obj.coins=newcoin
    #       obj.save()

    #       return redirect("/dashboard") 
    #   else:
    #          messages.warning(request, 'You dont have enough money for this transaction, Try selling some share .')
    #          return redirect("/dashboard") 
          
   

#_________________________________________________________________________________

def Dashboard(request):
     if request.session.has_key('uid'):          #check if session is created
      if 'uid' in request.session:              #to get data from session 
          alpha=request.session['uid']
      transaction=Transaction.objects.raw('SELECT * FROM home_Transaction WHERE username= %s' , [alpha])
      coinkadata=register.objects.raw('SELECT * FROM home_register WHERE username= %s',[alpha])
      context={
        'transaction':transaction,
        'coinkadata' :coinkadata
         }
      
      for u in transaction :
        print(u.username)
      return render(request,'dashboard.html',context)
     else :
        messages.warning(request, 'login to go to dashboard .')
        return render(request,'login.html')   