from django.views import View
from django.http import JsonResponse
import json
from .models import Rate

class RateAPIView(View):
    def get(self, request, dt):
        items_count = Rate.objects.count()
        items = Rate.objects.filter(data=dt)

        items_data = []
        
        items_data.append({
            "EUR": items.filter(nome="euro").get().cotacao,
            "BRL": items.filter(nome="real").get().cotacao,
            "JPY": items.filter(nome="iene").get().cotacao
        })

        cotacoes = {
            'data': dt,
            'base': 'USD',
            'rates': items_data
        }

        return JsonResponse(cotacoes)