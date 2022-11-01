from django.shortcuts import render
from .models import ImageHead
from cms.models import CmsSLider
from skills.models import Skills
from information.models import PersonalInformation


# Create your views here.
def resume_page(request):
    slider_list = CmsSLider.objects.all()
    imagehead = ImageHead.objects.get()
    #skills = {skill.skill: {'level': [x for x in range(skill.level)]} for skill in Skills.objects.all()}
    skills = Skills.objects.all()
    personal_information = PersonalInformation.objects.all()
    return render(request, './index.html', {'imagehead': imagehead,
                                            'slider_list': slider_list,
                                            'skills': skills,
                                            'personal_information': personal_information})
