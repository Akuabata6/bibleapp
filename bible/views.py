from django.shortcuts import render
from .models import Verse

def get_verse(request):
    verse_number= request.Get.get('verse_number')
    chapter_number = request.Get.get('chapter_number')
    #Get the requested verse
    verse = Verse.objects.filter(chapter=chapter_number, verse=verse_number).first()

    if verse:
        # Get the previous and next verse
        previous_verse = Verse.objects.filter(chapter=chapter_number, verse=verse_number - 1).first()
        next_verse = Verse.objects.filter(chapter=chapter_number, verse=verse_number + 1).first()

        return render(request, 'verse_detail.html', {
            'verse': verse,
            'previous_verse': previous_verse,
            'next_verse': next_verse,
        })
    else:
        return render(request, 'verse_not_found.html')  # Handle case when verse is not found
