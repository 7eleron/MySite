from django.shortcuts import render
from crm.models import ImageHead
from cms.models import CmsSLider
from skills.models import Skills
from information.models import PersonalInformation
from experience.models import Experience


# Create your views here.
def resume_page(request):
    slider_list = CmsSLider.objects.all()
    imagehead = ImageHead.objects.get()
    skills = {skill.skill: range(skill.level) for skill in Skills.objects.all()}
    # skills = Skills.objects.all()
    personal_information = PersonalInformation.objects.all()
    experience = Experience.objects.all()
    dict_data = {'imagehead': imagehead,
                 'slider_list': slider_list,
                 'skills': skills,
                 'personal_information': personal_information,
                 'experience': experience,
    }
    return render(request, './index.html', dict_data)
