from django.shortcuts import render
import datetime
#import json response
from django.http.response import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

        ## If the age is 35 perctange is 50% and 
        perc = age / 70 * 100;
        ## perc to fixes 2
        perc = round(perc, 2)

        ## 0-25 25-50 50-75 75-100 for perc
        if perc >= 0 and perc <= 25:
            quote = "Zamanla nasıl değişiyor insan hangi resmime baksam ben değilim!"
        elif perc >= 25 and perc <= 50:
            quote = "Gökyüzünün başka rengi de varmış! \n Geç fark ettim taşın sert olduğunu."
        elif perc >= 50 and perc <= 75:
            quote = "Yaş 35 yolun yarısı eder. \n Dante gibi ortasındayız ömrün." 
        else:
            quote = "Ne dönüp duruyor havada kuşlar?\n Nerden çıktı bu cenaze? Ölen kim?"

        ## Age conditions
        if age == 18:
            quote = "Delikanlı çağımızdaki cevher, \n Yalvarmak, yakarmak nafile bugün."
        
        if age == 19:
            quote = "Hayal meyal şeylerden ilk aşkımız; \n Hâtırası bile yabancı gelir."

        if age == 20:
            quote = "Yalvarmak, yakarmak nafile bugün, \n Gözünün yaşına bakmadan gider."

        if age == 21:
            quote = "Her doğan günün bir dert olduğunu, \n İnsan bu yaşa gelince anlarmış."

        if age == 22:
            quote = "Hangi resmime baksam ben değilim \n Nerde o günler, o şevk, o heyecan?"

        if age == 23:
            quote = "Neden böyle düşman görünürsünüz; \n Yıllar yılı dost bildiğim aynalar?"

        if age >= 70:
            return render(request, 'dead.html')
        return render(request, 'result.html', {'age': age, 'perc': perc, 'birthdate': date_string, 'quote': quote})


    