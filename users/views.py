from django.shortcuts import render
from .models import Profile


def profiles(request):
    profileList = Profile.objects.all()
    context = {'profiles': profileList}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profileObj = Profile.objects.get(id=pk)
    topSkills = profileObj.skill_set.exclude(description__exact="")
    otherSkills = profileObj.skill_set.filter(description="")
    context = {'profile': profileObj, 'topSkills': topSkills, 'otherSkills': otherSkills}
    return render(request, 'users/user-profile.html', context)

