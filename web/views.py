from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense, Income
from datetime import datetime
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@csrf_exempt
def submit_expense(request):
    #User submits an expense

    #TODO: validate data, user might be fake, token might be...
    this_token = request.POST['token']
    this_token_id = Token.objects.filter(key=this_token).values('user_id').first().get('user_id')
    this_user = User.objects.filter(id= this_token_id).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Expense.objects.create(user=this_user, date=date, amount=request.POST['amount'], text=request.POST['text'])
        
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)

@csrf_exempt
def submit_income(request):
        #User submits an income

    #TODO: validate data, user might be fake, token might be...
    this_token = request.POST['token']
    this_token_id = Token.objects.filter(key=this_token).values('user_id').first().get('user_id')
    this_user = User.objects.filter(id= this_token_id).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Income.objects.create(user=this_user, date=date, amount=request.POST['amount'], text=request.POST['text'])
        
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)

