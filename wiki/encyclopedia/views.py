from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from . import util

entrieslist = list(util.list_entries())
for i in range(len(entrieslist)):
    entrieslist[i] = entrieslist[i].lower()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": entrieslist
    })

def entry(request, name): 
    if name not in entrieslist:
        return render(request, "encyclopedia/entry.html") 
    return render(request, "encyclopedia/entry.html", {
        "entries": util.list_entries(),
        "name": name.lower()
            })
    
def create(request): 
    return render(request, "encyclopedia/create.html")

def redirect_view(request):
    response = redirect('/create')
    return response
