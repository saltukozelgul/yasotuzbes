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
        ## Calculate the total days
        total_days = (datetime.datetime.now() - date).days 
        perc = total_days / 25500 * 100;
        ## perc to fixes 2
        perc = round(perc, 2)

        ## read json file
        data = {}
        with open('yasotuzbes/quotes/data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)


        ## For main auidence
        if age >= 18 and age <= 23:
            pass
        else:
            # for not detailed ages
            if perc >= 0 and perc <= 25:
                age = 1
                quarter = 1
            elif perc >= 25 and perc <= 50:
                age = 24
                quarter = 1
            elif perc >= 50 and perc <= 75:
                age = 40
                quarter = 1
            elif perc >= 75 and perc <= 100:
                age = 100
                quarter = 1
            else:
                return render(request, 'dead.html')

        # read json and inc counter
        with open('yasotuzbes/datas/counter.json', 'r', encoding='utf-8') as f:
            counter = json.load(f)
            counter['counter'] += 1
        # write json
        with open('yasotuzbes/datas/counter.json', 'w', encoding='utf-8') as f:
            json.dump(counter, f, indent=4, ensure_ascii=False)
        return render(request, 'result.html', {'age': age, 'perc': perc, 'birthdate': date_string, 'quote': data[f"{age}.{quarter}"], 'counter': counter['counter']})


    