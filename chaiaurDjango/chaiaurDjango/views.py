from django.http import HttpResponse
from django.shortcuts import render


def home(request):
     #return HttpResponse(" hii django sup")
    return render(request, 'layout.html')
def about(request):
    return HttpResponse("  django about info") 

def contact(request):
    return HttpResponse(" hii django contact karo")