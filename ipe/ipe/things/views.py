from django.shortcuts import render, get_object_or_404

from things.models import Thing


# Create your views here.
def detail(request, id):
    thing = get_object_or_404(Thing, pk=id)
    return render(request, "things/details.html", {"thing": thing})
