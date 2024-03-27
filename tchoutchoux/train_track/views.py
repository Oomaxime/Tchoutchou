from django.shortcuts import render
from django.http import HttpResponse
from train_track.models import Train


def index(request):
    ATrain = Train.objects.all()
    return render(request, "train_track/index.html", {
        "Train": ATrain,
    })


def show(request):
    return render(request, "train_track/show.html", {})


def random(request):
    return render(request, "train_track/random.html", {})
