from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json



def RecordedVideoHit(request, options):


    return render(request, 'SubTemplates/RecordedVideoHit.html', {'options': options})