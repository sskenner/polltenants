# best/models.py

from django.db import models 


class Team(models.Model): 
    team_name = models.CharField(max_length=40) 

    TEAM_LEVELS = (
        ('U09', 'Under 09s'),
        ('U10', 'Under 10s'),
        ('U11', 'Under 11s'),
        ...  # list our other teams
    )
    team_level = models.CharField(max_length=3, choices=TEAM_LEVELS, default='U11')

# best/views.py


from django.shortcuts import render
from .models import Team 


def youngest(request):
    list_teams = Team.objects.filter(team_level__exact="U09")
    context = {'youngest_teams': list_teams}
    return render(request, 'best/index.html', context)
