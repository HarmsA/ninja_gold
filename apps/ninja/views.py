from django.shortcuts import render, redirect, HttpResponse
from datetime import datetime
from random import randint

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'location_list' not in request.session:
        request.session['location_list'] = []

    return render(request,'ninja/main.html')

def process(request):
    if request.method != 'POST':
        return HttpResponse('Issue with method type.')

    context = {'farm': randint(10,20),
               'cave': randint(5,10),
               'house': randint(2,5),
               'casino': randint(-50,50),
               }
    request.session['gold'] += context[request.POST['location']]
    date = datetime.now()
    request.session['datetime'] = date.strftime("%Y-%m-%d %H:%M:%S")

    visit_list = request.session['location_list']
    visit_list.append({'place': f'Earned {context[request.POST["location"]]} in '
                        f'the {request.POST["location"]}!'
                        f' {request.session["datetime"]}'})

    request.session['location_list'] = visit_list
    return redirect('/')