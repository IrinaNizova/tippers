from django.shortcuts import render
from .models import CurrentTrip, TipperModels


def tippers(request):

    tippers = CurrentTrip.objects.all()
    if 'model_title' in request.GET and request.GET['model_title']:
        tippers = tippers.filter(machine__model__title=request.GET['model_title'])
    return render(request, 'tippers.html', {'tippers': tippers,
                                            'models': TipperModels.objects.all()})
