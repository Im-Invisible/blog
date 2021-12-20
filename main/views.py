from django.shortcuts import render

def index(request):
    data = {
        'title': 'Invisible blog',        
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

