from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Game

def games_list(request):
    games = Game.objects.all()
    # Mock data if database is empty for testing
    if not games.exists():
        games = [{
            'title': 'Neon Snake',
            'slug': 'snake',
            'description': 'A retro classic reborn with a sleek neon aesthetic. Eat the glowing dots to grow, but do not crash into yourself!',
            'cover_image_url': 'https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&w=800&q=80',
            'template_name': 'games/snake.html'
        }]
    return render(request, 'games/list.html', {'games': games})

def play_game(request, slug):
    try:
        game = Game.objects.get(slug=slug)
    except Game.DoesNotExist:
        # Mock for testing
        if slug == 'snake':
            game = {
                'title': 'Neon Snake',
                'description': 'A retro classic reborn with a sleek neon aesthetic.',
                'template_name': 'games/snake.html'
            }
        else:
            raise Http404("Game not found")
            
    return render(request, 'games/play.html', {'game': game})
