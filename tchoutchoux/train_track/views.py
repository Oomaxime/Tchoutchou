from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "train_track/index.html", {

    })


def show(request):
    return render(request, "train_track/show.html", {})


def random(request):
    return render(request, "train_track/random.html", {})
