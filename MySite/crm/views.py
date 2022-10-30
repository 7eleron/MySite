from django.shortcuts import render
from .models import ImageHead
from cms.models import CmsSLider


# Create your views here.
def resume_page(request):
    slider_list = CmsSLider.objects.all()
    imagehead = ImageHead.objects.get()
    return render(request, './index.html', {'imagehead': imagehead,
                                            'slider_list': slider_list})
