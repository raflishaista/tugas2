from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Sheoldred, the Apocalypse',
        'amount': 2,
        'description': 'Magic: the Gathering',
        'name2': 'Mirrorjade the Iceblade Dragon',
        'amount2': 3,
        'description2':"Yu-Gi-Oh!"

    }

    return render(request, "main.html", context)
# Create your views here.
