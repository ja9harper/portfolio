from django.shortcuts import render

# Create your views here.
def janine(request):
    return render(request, 'jobs/janine.html')
