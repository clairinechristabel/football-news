from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406359941',
        'name': 'Clairine Christabel Lim',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
