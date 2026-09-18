import json
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Game, Score
from .forms import GameUploadForm

def games_list(request):
    games = Game.objects.all().order_by('-id')
    return render(request, 'games/list.html', {'games': games})

@login_required
def developer_dashboard(request):
    if request.method == 'POST':
        form = GameUploadForm(request.POST)
        if form.is_valid():
            game = form.save()
            return redirect('play_game', slug=game.slug)
    else:
        form = GameUploadForm()
    return render(request, 'games/dashboard.html', {'form': form})

def play_game(request, slug):
    game = get_object_or_404(Game, slug=slug)
    top_scores = game.scores.all()[:10]
    if game.template_name == 'games/play_python.html':
        return render(request, 'games/play_python.html', {'game': game, 'top_scores': top_scores})
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
