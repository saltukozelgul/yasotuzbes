import json
import os
from django.shortcuts import render
import datetime
#import json response
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def calcalateQuater(month):
    if month >= 1 and month <= 3:
        return 1
    elif month >= 4 and month <= 6:
        return 2
    elif month >= 7 and month <= 9:
        return 3
    else:
        return 4

def result(request):
    if request.method == "POST":
        data = request.POST.get('birthdate')
        # create date object
        date = datetime.datetime.strptime(data, '%Y-%m-%d')
        date_string = date.strftime('%d %B %Y') 

        # replace January with Ocak
        #  I know its terrible xd. I will fix it later
        date_string = date_string.replace('January', 'Ocak')
        date_string = date_string.replace('February', 'Şubat')
        date_string = date_string.replace('March', 'Mart')
        date_string = date_string.replace('April', 'Nisan')
        date_string = date_string.replace('May', 'Mayıs')
        date_string = date_string.replace('June', 'Haziran')
        date_string = date_string.replace('July', 'Temmuz')
        date_string = date_string.replace('August', 'Ağustos')
        date_string = date_string.replace('September', 'Eylül')
        date_string = date_string.replace('October', 'Ekim')
        date_string = date_string.replace('November', 'Kasım')
        date_string = date_string.replace('December', 'Aralık')

        ## calculate the age
        age = datetime.datetime.now().year - date.year
        quarter = calcalateQuater(date.month)
        ## If the age is 35 perctange is 50% and 
        perc = age / 70 * 100;
        ## perc to fixes 2
        perc = round(perc, 2)

        ## read json file
        data = {}
        with open('yasotuzbes/quotes/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        ## 0-25 25-50 50-75 75-100 for perc
                ## For main auidence
        if age >= 18 and age <= 23:
            pass
        else:
            if perc >= 0 and perc <= 25:
                age = 1
            elif perc >= 25 and perc <= 50:
                age = 24
            elif perc >= 50 and perc <= 75:
                age = 40
            else:
                age = 100








        ## json formak of quoteos
        #quoteos = {
        #    "quote": quote
        #}

        if age >= 70:
            return render(request, 'dead.html')
        return render(request, 'result.html', {'age': age, 'perc': perc, 'birthdate': date_string, 'quote': data[f"{age}.{quarter}"]})


    