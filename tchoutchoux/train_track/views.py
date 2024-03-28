from django.shortcuts import render
from django.http import HttpResponse
from train_track.models import Train


def index(request):
    ATrain = Train.objects.all()
    return render(request, "train_track/index.html", {
        "Train": ATrain,
    })


def show(request, train_ID):
    myTrain = Train.objects.get(trainID=train_ID)
    return render(request, "train_track/show.html", {
        "name": myTrain.name,
        "destination": myTrain.destination,
        "date_start": myTrain.date_start,
        "date_end": myTrain.date_end,
        "plan": myTrain.plan,
    })


def random(request):
    return render(request, "train_track/random.html", {})
