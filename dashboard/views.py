from django.shortcuts import render

# Create your views here.
def dasboardView(request):
    context = {

    }
    return render(request, "dashboard.html", context)