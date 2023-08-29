from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense, Income, Token, User
from datetime import datetime

@csrf_exempt
def submit_expense(request):
    #User submits an expense

    #TODO: validate data, user might be fake, token might be...
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token= this_token).get()
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
    this_user = User.objects.filter(token__token= this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']
    Income.objects.create(user=this_user, date=date, amount=request.POST['amount'], text=request.POST['text'])
        
    return JsonResponse({
        'status': 'ok',
    }, encoder=JSONEncoder)