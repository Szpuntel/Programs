from django.shortcuts import render, get_object_or_404
from projekty.sklep.Produkty.models import Produkty
from .models import Profile



def my_profile(request):
    my_user_profile = Profile.objects.filter(user=request.user).first()
    my_orders = Produkty.objects.filter(is_ordered=True, owner=my_user_profile)
    context = { 'my_orders': my_orders }

    return render(request, 'profile.html', context)
