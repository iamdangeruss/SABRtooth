from django.shortcuts import render
from django.http import HttpResponse
from SABR.models import Master, Batting
from SABR.forms import MasterForm





def index(request):
    
    return render(request, 'sabr/index.html')
    
def player(request, playerid):
    context_dict = {}
    #player_list = Master.objects.order_by('namelast')[:25]
    #batting_list = Batting.objects.order_by('yearid')[:25]
    #context_dict = {'players': player_list,'battinglines': batting_list}
    
    player = Master.objects.get(playerid=playerid)
    #context_dict['player_name'] = player.namefirst
    #context_dict = ['player'] = player
    
    
    batting_list = Batting.objects.filter(playerid=playerid)
    #context_dict = ['batting_list']= batting_list
    
    context_dict = {'player': player,'battinglines': batting_list}
    
    # Render the response and send it back!
    return render(request, 'sabr/player.html', context_dict)
    

    
    
def search(request):
    error = False
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        if not q:
            error = True
        else:
            players = Master.objects.filter(player_fullname__icontains=q) 
            return render(request, 'sabr/search_results.html',
                {'players': players, 'query': q})
    
    return render(request, 'sabr/search_form.html', {'error': error})  
    
# BAD!
def bad_search(request):
    # The following line will raise KeyError if 'q' hasn't
    # been submitted!
    message = 'You searched for: %r' % request.GET['q']
    return HttpResponse(message)          

    
    

    