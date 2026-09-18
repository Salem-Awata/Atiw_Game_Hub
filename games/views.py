from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Game

def games_list(request):
    games = Game.objects.all()
    # Mock data if database is empty for testing
    if not games.exists():
        games = [
            {
                'title': 'Neon Snake',
                'slug': 'snake',
                'description': 'A retro classic reborn with a sleek neon aesthetic. Eat the glowing dots to grow, but do not crash into yourself!',
                'cover_image_url': '/static/images/snake_cover.jpg',
                'template_name': 'games/snake.html'
            },
            {
                'title': 'Brutal Pong',
                'slug': 'pong',
                'description': 'The grandfather of video games with a raw, high-contrast brutalist edge. Defeat the AI or a friend locally.',
                'cover_image_url': '/static/images/pong_cover.jpg',
                'template_name': 'games/pong.html'
            },
            {
                'title': 'Block Drop',
                'slug': 'tetris',
                'description': 'Stack falling blocks to clear lines and rack up a massive high score. Fast, unforgiving, addictive.',
                'cover_image_url': '/static/images/tetris_cover.jpg',
                'template_name': 'games/tetris.html'
            }
        ]
    return render(request, 'games/list.html', {'games': games})

def play_game(request, slug):
    try:
        game = Game.objects.get(slug=slug)
    except Game.DoesNotExist:
        # Mock for testing
        mock_games = {
            'snake': {
                'title': 'Neon Snake',
                'description': 'A retro classic reborn with a sleek neon aesthetic.',
                'template_name': 'games/snake.html'
            },
            'pong': {
                'title': 'Brutal Pong',
                'description': 'The grandfather of video games with a raw, high-contrast brutalist edge.',
                'template_name': 'games/pong.html'
            },
            'tetris': {
                'title': 'Block Drop',
                'description': 'Stack falling blocks to clear lines and rack up a massive high score.',
                'template_name': 'games/tetris.html'
            }
        }
        if slug in mock_games:
            game = mock_games[slug]
        else:
            raise Http404("Game not found")
            
    return render(request, 'games/play.html', {'game': game})
