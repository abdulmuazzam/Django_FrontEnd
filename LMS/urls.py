from django.urls import path
from . import views,SubViews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.RLMS_Welcome, name='RLMS'),
    path('MainPage', views.MainPage, name='MainPage'),
    path('MainPage/LoadRoutine', views.LoadMenu, name='LoadPage'),
    path('MainPage/viewRoutine', views.viewRoutine, name='viewRoutine'),
    path('MainPage/Routines', views.RoutinesMenu, name='NewRoutinesPage'),
    path('MainPage/ManageRoutines', views.ManageRoutinesMenu, name='ManageRoutines'),


    path('MainPage/Routines/RecordedVideo/<str:options>', SubViews.RecordedVideoHit, name='RecordedVideo'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


