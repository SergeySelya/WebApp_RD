from django.shortcuts import render
from .models import Post_0, Post_1, Post_2, Post_3, Post_4, Post_5


def index(request):
    info_0 = Post_0.objects.all()
    info_1 = Post_1.objects.all()
    info_2 = Post_2.objects.all()
    info_3 = Post_3.objects.all()
    info_4 = Post_4.objects.all()
    info_5 = Post_5.objects.all()

    return render(request, 'main/main.html', {"info_0": info_0, "info_1": info_1,
                                              "info_2": info_2, "info_3": info_3,
                                              "info_4": info_4, "info_5": info_5})


def form0(request):
    info_0 = Post_0.objects.all()

    return render(request, 'main/form0.html', {"info_0": info_0})


def form1(request):
    info_1 = Post_1.objects.all()

    return render(request, 'main/form1.html', {"info_1": info_1})


def form2(request):
    info_2 = Post_2.objects.all()

    return render(request, 'main/form2.html', {"info_2": info_2})


def form3(request):
    info_3 = Post_3.objects.all()

    return render(request, 'main/form3.html', {"info_3": info_3})


def form4(request):
    info_4 = Post_4.objects.all()

    return render(request, 'main/form4.html', {"info_4": info_4})


def form5(request):
    info_5 = Post_5.objects.all()

    return render(request, 'main/form5.html', {"info_5": info_5})

