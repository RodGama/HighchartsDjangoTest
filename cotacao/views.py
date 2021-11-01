import http.client

from datetime import timedelta, date

import json

from django.shortcuts import render

from .models import Rate



def home(request):

    cotacoes = Rate.objects.all().order_by('-data')

    if cotacoes.count() == 0:

        for x in range(1,6):

            dataBusca =  ((date.today()) + timedelta(days=1-x)).strftime('%Y-%m-%d')

            conn = http.client.HTTPSConnection("api.vatcomply.com")

            payload = ''

            headers = {}

            conn.request("GET", "/rates?base=USD&date=" + dataBusca, payload, headers)

            res = conn.getresponse()
            data = res.read()

            dados = json.loads(data)

            euro = Rate.objects.create(nome ='euro', cotacao = dados['rates']['EUR'], data = dados['date'])

            real = Rate.objects.create(nome ='real', cotacao = dados['rates']['BRL'], data = dados['date'])

            iene = Rate.objects.create(nome ='iene', cotacao = dados['rates']['JPY'], data = dados['date'])

            euro.save()

            real.save()

            iene.save()

    elif cotacoes[0].data < (date.today()):

        hoje = (date.today()).strftime('%Y-%m-%d')

        conn = http.client.HTTPSConnection("api.vatcomply.com")

        payload = ''

        headers = {}

        conn.request("GET", "/rates?base=USD&date=" + hoje, payload, headers)

        res = conn.getresponse()
        data = res.read()

        dados = json.loads(data)

        euro = Rate.objects.create(nome ='euro', cotacao = dados['rates']['EUR'], data = dados['date'])

        real = Rate.objects.create(nome ='real', cotacao =dados['rates']['BRL'], data = dados['date'])

        iene = Rate.objects.create(nome ='iene', cotacao =dados['rates']['JPY'], data = dados['date'])

        euro.save()

        real.save()

        iene.save()

    cotacoes = Rate.objects.all()

    cotacoesEuro = cotacoes.filter(nome='euro').order_by("data")

    cotacoesIene = cotacoes.filter(nome='iene').order_by("data")

    cotacoesReal = cotacoes.filter(nome='real').order_by("data")

    dictEuro = [{'timestamp' : cotacao.data ,'cotacao' : f'{cotacao.cotacao}'.replace(",",".")} for cotacao in cotacoesEuro] 

    dictIene = [{'timestamp' : cotacao.data ,'cotacao' : f'{cotacao.cotacao}'.replace(",",".")} for cotacao in cotacoesIene] 

    dictReal = [{'timestamp' : cotacao.data ,'cotacao' : f'{cotacao.cotacao}'.replace(",",".")} for cotacao in cotacoesReal] 
    

    context  = {'cotacoesEuro' : dictEuro, 'cotacoesIene': dictIene, 'cotacoesReal' : dictReal}
    

    return render(request, 'home.html', context)

