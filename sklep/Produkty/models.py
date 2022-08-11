from tabnanny import verbose
from unicodedata import decimal
from django.db import models
from PIL import Image



class Kategoria (models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


# Rejestrujemy widok w admin.py
class Producent (models.Model):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=244)
    opis = models.TextField(blank=True)

    class Meta:
        verbose_name = "Producent"
        # models.py to plik odpowiedzialny za Baze Danych !
        verbose_name_plural = "Producenci"
        # Jedna Klasa w tym pliku odpowiada jednej tabeli w bazie.


class Produkty(models.Model):
    kategoria = models.ForeignKey(
        Kategoria, on_delete=models.CASCADE, blank=True, null=True)
    # CharField Odpowiadnik "Input text" z formularzy w HTML'u.
    nazwa = models.CharField(max_length=100)
    # TextField Odpowiadnik "Text Area" z formularzy w HTML'u. (blank=True) - Opis nie jest obowiązkowy.
    opis = models.TextField(blank=True)
    # Max 12 cyfr, 2 liczby po przecinku.
    cena = models.DecimalField(max_digits=12, decimal_places=2)
    producent = models.ForeignKey(
        Producent, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='product_pics')

    # Pamietaj aby dodać aplikacje do Skelp/settings.py/ (jednorazowo)
    # Pamietaj w admin.py "from .models import Produkty" i "admin.site.register(Produkty)"
    def __str__(self):
        # Po każdej zmianie w tym pliku należy przeprowadzić migracje "python manage.py makemigrations"
        return self.nazwa
        # __str__(self) wyswitla nazwe produktu.
    
    def short_opis(self):
        return self.opis(0, 50)

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # Meta sprawia ze na Admin site wyswitla sie "Produkty" a nie "Produktys"
    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"
