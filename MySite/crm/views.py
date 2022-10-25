from django.shortcuts import render
from .models import ImageHead


# Create your views here.
def resume_page(request):
    imagehead = ImageHead.objects.get()
    return render(request, './index.html', {'imagehead': imagehead})
