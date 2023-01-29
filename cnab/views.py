from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Cnab
from django.db import models

def list_operations(request):
    get_operations = Cnab.objects.all()
    total_saldo = Cnab.objects.aggregate(models.Sum('amount'))
    return render(request, 'cnab/list.html', {'operacoes': get_operations, 'total_saldo': total_saldo})

def upload_file(request):
    if request.method == 'POST':
        with open("CNAB.txt", "wb") as file:
            for chunk in request.FILES["file"].chunks():
                file.write(chunk)

        path = "CNAB.txt"
        with open(path, "r", encoding="utf-8") as cnab_read:
            lista = []
            for line in cnab_read.read().split("\n"):
                lista.append(line)

        for li in lista:
            type = li[0]
            date = li[1:9]
            amount = li[9:19]
            cpf = li[19:30]
            card = li[30:42]
            hour = li[42:48]
            owner = li[48:62]
            store = li[62:]

            Cnab.objects.create(
                type = type,
                date = date,
                amount = amount,
                cpf = cpf,
                card = card,
                hour = hour,
                owner = owner,
                store = store
        )
        return HttpResponseRedirect('lista/')
    else:
        return render(request, 'cnab/upload.html')
    