from django.shortcuts import render


def helps(request):
    return render(request, 'help.html')
