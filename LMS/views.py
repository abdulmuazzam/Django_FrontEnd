from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json

# Create your views here.


def RLMS_Welcome(request):
    # return HttpResponse('<h1>Succeeded !!!!</h1>')

    title = 'Programming Industrial Cobots Using Natural User Interactions (PICNUI)' 
    desc = 'Robot, any automatically operated machine that replaces human effort, though it may not resemble human beings in appearance or perform functions in a humanlike manner. By extension, robotics is the engineering discipline dealing with the design, construction, and operation of robots.'

    Profile_1 = models.Profile()
    Profile_2 = models.Profile()
    Profile_3 = models.Profile()
    Profile_4 = models.Profile()
    Profile_5 = models.Profile()

    Profile_1.Name = 'Abdul Muazzam'
    Profile_1.Data = 'SP17-BSE-033'
    Profile_1.ImgUrl = 'Images/BG.jpeg'

    Profile_2.Name = 'Faizan Haider'
    Profile_2.Data = 'SP17-BSE-108'
    Profile_2.ImgUrl = 'Images/BG.jpeg'

    Profile_3.Name = 'Adeel Arshad'
    Profile_3.Data = 'SP17-BSE-132'
    Profile_3.ImgUrl = 'Images/BG.jpeg'

    Profile_4.Name = 'Dr. Wajaht'
    Profile_4.Data = 'Supervisor'
    Profile_4.ImgUrl = 'Images/BG.jpeg'

    Profile_5.Name = 'Dr. Aksam'
    Profile_5.Data = 'Co. Supervisor'
    Profile_5.ImgUrl = 'Images/BG.jpeg'



    Profile_List = [Profile_1, Profile_2, Profile_3]
    Supervisor_Profile_List = [Profile_4, Profile_5]
    ProgressValue = [30,50,70,90]

    return render(request, 'LMS_Welcome.html', {'ProjectTitle': title, 'ProjectDescription': desc, 'Profiles': Profile_List, 'SupervisorProfile': Supervisor_Profile_List, 'ProgressBarStatus': ProgressValue})



def MainPage(request):


    return render(request, 'MainPage.html')

def LoadMenu(request):
    routinesData = ['Routine1', 'Routine2', 'Routine3','Routine3','Routine3','Routine3','Routine3','Routine3','Routine3','Routine3','Routine3','Routine3','Routine3','Routine3',]

    routinesList = []

    for i in range(15):
        routinesList.append(models.Routine('UR Routine', [{'x': 2,'y':4,'z':3}], 'Moazzam'))

    return render(request, 'LoadRoutine.html', {'routines': routinesList})

def viewRoutine(request):



    # name = request.GET.get('Name')
    # x =  request.GET.get('X')
    # y =  request.GET.get('Y')
    # z =  request.GET.get('Z')
    # capturededBy =  request.GET.get('CapturingPerson')

    # models.Routine(name,[x,y,z], capturededBy)

    return render(request, 'viewRoutine.html')

def RoutinesMenu(request):
    print('Testing : ',request.session.get('option', None))
    # print(option)
    return render(request, 'NewRoutines.html')

def ManageRoutinesMenu(request):
    routinesList = []

    for i in range(15):
        routinesList.append(models.Routine('UR Routine', [2, 4, 3], 'Moazzam'))

    return render(request, 'ManageRoutines.html', {'routines': routinesList})
