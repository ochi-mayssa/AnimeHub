from manga.models import Manga
from anime.models import Anime
def base_content(request):
    return {
        'trending_anime': Anime.objects.order_by('-rating')[:6],
        'top_manga': Manga.objects.order_by('-rating')[:4]
    }
def global_genres(request):
    return {
        'anime': Anime.objects.all(),
        'manga': Manga.objects.all()
    }