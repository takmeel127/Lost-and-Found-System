from django.shortcuts import render

def starter(request):
    return render(request, 'starter.html')
