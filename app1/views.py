<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def home_page(request):
    user=None
    if 'user_id' in request.session:
        try:
            user=UserClass.objects.get(user_id=request.session['user_id'])

        except UserClass.DoesNotExist:
            del request.session['user_id']
            user=None

    ad_obj=BankAd.objects.all()
    return render(request,'homepage.html',{'ad_data':ad_obj,'user_data':user})


def add_user(request):
    acc_type = AccountType.objects.all()
    if request.method=="POST":
        print(request.POST)
        user_obj=UserClass()
        user_obj.user_first_name=request.POST['firstname']
        user_obj.user_last_name=request.POST['lastname']
        user_obj.user_sex=request.POST['usersex']

        dob_str = request.POST['userdob']
        user_obj.user_dob = datetime.strptime(dob_str, '%Y-%m-%d')
        current_date=datetime.now()
        age=current_date.year-user_obj.user_dob.year-((current_date.month,current_date.day)<(user_obj.user_dob.month,user_obj.user_dob.day))
        user_obj.user_age=age

        user_obj.user_email=request.POST['useremail']
        user_obj.user_mobile=request.POST['usermobile']
        user_obj.user_address=request.POST['useraddress']
        user_obj.user_state=request.POST['userstate']
        user_obj.user_city=request.POST['usercity']
        user_obj.user_pincode=request.POST['userpincode']
        user_obj.acc_type=AccountType.objects.get(acc_type=request.POST['useraccount'])
        user_obj.user_password=request.POST['password']


        user=UserClass.objects.filter(user_email=user_obj.user_email,user_mobile=user_obj.user_mobile).first()

        if user:
            return render(request, 'boiregister.html', {'acc_type_data': acc_type,'response':'User email and mobile already exist!'})

        else:
            user_obj.save()
            request.session['user_id'] = user_obj.user_id
            return render(request,'useraccountnumber.html',{'user_data':user_obj})

    return render(request,'boiregister.html',{'acc_type_data':acc_type})

def user_login(request):
    if request.method=="POST":
        print("POST data:", request.POST)
        user_id=request.POST['account_number']
        user_password=request.POST['account_password']

        user=UserClass.objects.filter(user_id=user_id,user_password=user_password).first()
        print("User found:", user)

        if user:
            request.session['user_id']=user.user_id
            return redirect('/')

        else:
            response="Invalid username or password !"
            return render(request,'homepage.html',{'bank_response':response})

    return render(request,'homepage.html')

def user_logout(request):
    del request.session['user_id']
    return redirect('/')

def user_deposit(request):
    if 'user_id' in request.session:
        user_obj = UserClass.objects.get(user_id=request.session['user_id'])
        transaction=Transaction()
        if request.method=='POST':
            deposit=request.POST['deposit']
            deposit=int(deposit)
            user_obj.user_balance+=deposit
            user_obj.save()

            transaction.transaction_amount=deposit
            transaction.transaction_method="+"
            transaction.transaction_details="deposited"
            transaction.user=user_obj
            transaction.save()
            return render(request,'transaction.html',)
        return render(request,'bankdeposit.html',{'user_data':user_obj})
    else:
        return HttpResponse("Please login to continue!")

def user_withdrawal(request):
    if 'user_id' in request.session:
        user_obj=UserClass.objects.get(user_id=request.session['user_id'])
        if request.method=='POST':
            print(request.POST)
            withdrawal=int(request.POST['withdrawal'])
            request.session['withdrawal']=withdrawal
            print(withdrawal)
            return redirect('withdrawal_confirm')
        return render(request,'bankwithdrawal.html',{'user_data':user_obj})
    else:
        return HttpResponse("Please login to continue!")

def withdrawal_confirm(request):
    if 'user_id' in request.session:
        user = UserClass.objects.get(user_id=request.session['user_id'])
        transaction = Transaction()

        if 'withdrawal' in request.session:
            withdrawal_amount = int(request.session['withdrawal'])

            if request.method == 'POST':
                print(request.POST)
                user_password = request.POST.get('password')

                if user.user_password == user_password:
                    print("hi")
                    if user.user_balance - withdrawal_amount >= user.acc_type.min_balance:
                        print("hello")
                        check=user.user_balance-withdrawal_amount #minimum balance checking
                        print(check)

                        user.user_balance -= withdrawal_amount
                        user.save()

                        transaction.transaction_amount = withdrawal_amount
                        transaction.transaction_method = "-"
                        transaction.transaction_details = "withdrawn"
                        transaction.user = user
                        transaction.save()

                        del request.session['withdrawal']
                        return render(request, 'transaction.html')

                    else:
                        print("hw r u")
                        response = "Not enough balance for this transaction (minimum balance required)."
                        return redirect('user_withdrawal')

                else:
                    response = "Incorrect Password!"
                    return render(request, 'bankpassword.html', {'response': response, 'user_data': user})

            return render(request, 'bankpassword.html', {'user_data': user})

    else:
        return redirect('/')


def user_transfer(request):
    if 'user_id'in request.session:
        user=UserClass.objects.get(user_id=request.session['user_id'])
        if request.method=='POST':
            print(request.POST)
            recipient_account_number=request.POST.get('recipient_account_number')
            try:
                recipient=UserClass.objects.get(user_id=recipient_account_number)
                request.session['recipient_number']=recipient.user_id
                return redirect('transfer_details')

            except UserClass.DoesNotExist:
                response="Invalid recipient account number!"
                return render(request,'banktransfer.html',{'response':response})
        return render(request,'banktransfer.html')
    else:
        return HttpResponse("Please login to continue!")

def transfer_details(request):
    if 'user_id' in request.session:
        user=UserClass.objects.get(user_id=request.session['user_id'])
        if 'recipient_number' in request.session:
            recipient=UserClass.objects.get(user_id=request.session['recipient_number'])
            if request.method=='POST':
                print(request.POST)
                amount=request.POST.get('amount')
                request.session['amount']=amount
                return redirect('transfer_confirm')
            return render(request,'recipientconfirm.html',{'recipient_data':recipient})
    else:
        return HttpResponse("Please login to continue!")

def transfer_confirm(request):
    if 'user_id' in request.session:
        user=UserClass.objects.get(user_id=request.session['user_id'])
        recipient=UserClass.objects.get(user_id=request.session['recipient_number'])
        transaction=Transaction()

        if request.method=='POST':
            print(request.POST)
            user_password=request.POST.get('password')
            if user.user_password==user_password:
                print("Entered password block")
                amount=int(request.session['amount'])
                if user.user_balance-amount>=user.acc_type.min_balance:
                    print("entered min balance block")
                    check=user.user_balance-amount
                    print(check)#checking minimum balance

                    user.user_balance-=amount
                    user.save()
                    recipient.user_balance+=amount
                    recipient.save()

                    debit_transaction = Transaction(
                        transaction_method="-",
                        transaction_amount=amount,
                        transaction_details=f"transferred to {recipient}",
                        user=user
                    )
                    debit_transaction.save()

                    credit_transaction = Transaction(
                        transaction_method="+",
                        transaction_amount=amount,
                        transaction_details=f"transferred from {user}",
                        user=recipient
                    )

                    credit_transaction.save()

                    del request.session['amount']
                    del request.session['recipient_number']

                    return render(request,'transaction.html')

                else:
                    response="Not enough balance for this transaction"
                    return render(request,'recipientconfirm.html',{'response':response,'recipient_data':recipient})

            else:
                response="Incorrect Password!"
                return render(request,'bankpassword.html',{'response':response,'user_data':user})

        return render(request,'bankpassword.html')

def transaction_history(request):
    if 'user_id' in request.session:
        transaction=Transaction.objects.filter(user_id=request.session['user_id'])
        return render(request,'tansactionhistory.html',{'transaction':transaction})
    return HttpResponse("Please login to continue!")
=======
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import *

# Create your views here.
from django.http import HttpResponse

def ajio_home(request):
    gender_obj=Gender.objects.all()
    men_obj=ClothType.objects.filter(gender__gender_id=1)
    women_obj=ClothType.objects.filter(gender__gender_id=2)
    boys_obj=ClothType.objects.filter(gender__gender_id=3)
    girls_obj=ClothType.objects.filter(gender__gender_id=4)
    return render(request,'ajiohome.html',{'data':gender_obj,'men_data':men_obj,'women_data':women_obj,"boy_data":boys_obj,"girl_data":girls_obj})

def user_register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')

        existing_user=User.objects.get(username=username)

        if existing_user:
            return render(request,'login.html')

        if not existing_user:
            user=User.objects.create_user(username=username,password=password,email=email)

>>>>>>> 7cb7e58 (clothmate added)
