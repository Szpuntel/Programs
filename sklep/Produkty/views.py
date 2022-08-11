from django.shortcuts import render
from django.http import HttpResponse      # importujemy biblioteke HttpResponse w celu uzycia jej do zwrócenia zawartości zapytania
from .models import Produkty, Kategoria, Producent              # importujemy modele produktów.

def index(request):                        # W pliku Sklep/urls.py importujemy"from Produkty.views imoprt index i dodajemy path z nazwą funkcji"
   # wszystkie = Produkty.objects.all()   # Kwerenda dla bazy danych ktora oznacza to samo co SELECT * FROM Produkty
    kategorie = Kategoria.objects.all()            # jeden = Produkty.objects.get(pk=1)
    dane = {'kategorie': kategorie}
    return render(request, 'base.html', dane)     #Wysła dane do templatu  

def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria= kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user,
              'kategoria_produkt': kategoria_produkt,
              'kategorie': kategorie
              }
    return render(request, 'kategoria_produkt.html', dane)                      # Zwraca zawartość zapytania

def produkty(request, id):
    produkty_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all() 
    dane = {'produkt_user':produkty_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)
