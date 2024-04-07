from django.shortcuts import render
from django.http import HttpResponse
from train_track.models import Train
import random


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


def getrandom(request):
    GetAllTrains = Train.objects.all()
    select_train = random.choice(GetAllTrains)
    return render(request, "train_track/getrandom.html", {
        "name": select_train.name,
        "destination": select_train.destination,
        "date_start": select_train.date_start,
        "date_end": select_train.date_end,
        "plan": select_train.plan,
    })
