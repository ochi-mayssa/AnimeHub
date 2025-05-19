from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Manga, Chapter, Page

def manga_list(request):
    manga_list = Manga.objects.all().order_by('-rating')
    return render(request, 'manga/list.html', {'manga_list': manga_list})

def manga_detail(request, slug):
    manga = get_object_or_404(Manga, slug=slug)
    chapters = Chapter.objects.filter(manga=manga).order_by('-chapter_number')
    
    # Pagination
    paginator = Paginator(chapters, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'manga/detail.html', {
        'manga': manga,
        'page_obj': page_obj
    })

def chapter_view(request, slug, chapter_number):
    manga = get_object_or_404(Manga, slug=slug)
    chapter = get_object_or_404(Chapter, manga=manga, chapter_number=chapter_number)
    pages = Page.objects.filter(chapter=chapter).order_by('page_number')
    
    # Get adjacent chapters
    prev_chapter = Chapter.objects.filter(
        manga=manga, 
        chapter_number__lt=chapter_number
    ).order_by('-chapter_number').first()
    
    next_chapter = Chapter.objects.filter(
        manga=manga, 
        chapter_number__gt=chapter_number
    ).order_by('chapter_number').first()
    
    return render(request, 'manga/chapter.html', {
        'chapter': chapter,
        'pages': pages,
        'prev_chapter': prev_chapter,
        'next_chapter': next_chapter,
    })