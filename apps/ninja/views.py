from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from random import randint

# Create your views here.
def activities(request, location, money):
    mydate = datetime.now()
    formatedDate = mydate.strftime("%Y-%m-%d %H:%M:%S")
    request.session['datetime'] = formatedDate
    visit_list = request.session['visit_list']
    visit_list.append({'place':f'Earned {money} in the {location}! {formatedDate}'})
    return visit_list

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'visit_list' not in request.session:
        request.session['visit_list'] = []
    return render(request, 'ninja/main.html')

def process_money(request):
    if request.method != 'POST':
        return HttpResponse("Error, not 'POST'.")
    try:
        if request.POST['farm']:
            request.session['farm'] = request.POST['farm']
            money = randint(10,21)
            request.session['gold'] += money
            request.session['visit_list'] = activities(request, 'Farm', money)
    except:
        pass

    try:
        if request.POST['cave']:
            request.session['cave'] = request.POST['cave']
            money = randint(5,10)
            request.session['gold'] += money
            request.session['visit_list'] = activities(request, 'Cave', money)
    except:
        pass

    try:
        if request.POST['house']:
            request.session['house'] = request.POST['house']
            money = randint(2,5)
            request.session['gold'] += money
            request.session['visit_list'] = activities(request, 'House', money)
    except:
        pass

    try:
        if request.POST['casino']:
            request.session['casino'] = request.POST['casino']
            money = randint(-50,50)
            request.session['gold'] += money
            request.session['visit_list'] = activities(request, 'Casino', money)
    except:
        pass
    return redirect('/')