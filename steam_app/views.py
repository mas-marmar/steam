from django.shortcuts import render, HttpResponse

def hello(request):
    values = ["dklnh", "pomogite"]
    return render(request, 
                  'main.html',
                  {'values': values,
                   'is_draw_note': True})


