from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    return render(request, "main/count.html", {'fulltext': fulltext, 'count': len(wordlist)})