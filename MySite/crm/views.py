from django.shortcuts import render
from .models import ImageHead
from cms.models import CmsSLider
from skills.models import Skills


# Create your views here.
def resume_page(request):
    slider_list = CmsSLider.objects.all()
    imagehead = ImageHead.objects.get()
    skills = {skill.skill: [x for x in range(skill.level)] for skill in Skills.objects.all()}
    #skills = Skills.objects.all()
    return render(request, './index.html', {'imagehead': imagehead,
                                            'slider_list': slider_list,
                                            'skills': skills})
