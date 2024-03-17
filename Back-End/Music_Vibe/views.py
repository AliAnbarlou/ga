from django.shortcuts import render

def About(request):
    return render (request, 'all/base.html',{})

def Contact(request):
    return render (request, 'all/base.html',{})

def Home_Page(request):
    return render (request, 'index.html',{})

def custom_404_error_view(request, exception):
    return render(request, 'Errors/404.html', status=404)