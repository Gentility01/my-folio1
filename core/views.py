from django.shortcuts import render

# Create your views here.


def error_404(request, exception):
    return render(request, 'core/404.html')

def error_500(request):
    return render(request, 'core/500.html')