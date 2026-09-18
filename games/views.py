import json
from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Game, Score

def games_list(request):
    games = Game.objects.all()
    return render(request, 'games/list.html', {'games': games})

def play_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    top_scores = game.scores.all()[:10]
    return render(request, 'games/play.html', {'game': game, 'top_scores': top_scores})

@csrf_exempt
@require_POST
def submit_score(request, slug):
    game = get_object_or_404(Game, slug=slug)
    try:
        data = json.loads(request.body)
        initials = data.get('initials', '').upper()[:3]
        score = int(data.get('score', 0))
        
        if initials and score > 0:
            Score.objects.create(game=game, player_initials=initials, score=score)
            return JsonResponse({'status': 'success'})
        return JsonResponse({'status': 'invalid_data'}, status=400)
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
