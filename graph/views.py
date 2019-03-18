from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View

from rest_framework.views import APIView
from rest_framework.response import Response

from random import randint

# Create your views here.

default = []


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


class ChartData(APIView):
    def get(self, request, format=None):
        for i in range(1,15):
            default.append(randint(-15,15))
        labels = [i for i in range (1,16)]
        default_items = [*default]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)