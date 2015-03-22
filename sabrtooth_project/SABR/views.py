from django.shortcuts import render
from django.http import HttpResponse
from SABR.models import Master, Batting

def index(request):
    context_dict = {}
    #player_list = Master.objects.order_by('namelast')[:25]
    #batting_list = Batting.objects.order_by('yearid')[:25]
    #context_dict = {'players': player_list,'battinglines': batting_list}
    
    player = Master.objects.get(playerid="aaronha01")
    #context_dict['player_name'] = player.namefirst
    #context_dict = ['player'] = player
    
    
    batting_list = Batting.objects.filter(playerid="aaronha01")
    #context_dict = ['batting_list']= batting_list
    
    context_dict = {'player': player,'battinglines': batting_list}
    
    # Render the response and send it back!
    return render(request, 'sabr/index.html', context_dict)