from django.shortcuts import render
from django.http import JsonResponse
from .models import MotivationalPhrase
import random

# Create your views here.

def home(request):
    """Main page with form to select category"""
    categories = MotivationalPhrase.CATEGORY_CHOICES
    return render(request, 'phrases/home.html', {'categories': categories})

def about(request):
    """Project information page"""
    total_phrases = MotivationalPhrase.objects.count()
    categories_count = {}
    
    for category_code, category_name in MotivationalPhrase.CATEGORY_CHOICES:
        count = MotivationalPhrase.objects.filter(category=category_code).count()
        categories_count[category_name] = count
    
    context = {
        'total_phrases': total_phrases,
        'categories_count': categories_count,
        'categories': MotivationalPhrase.CATEGORY_CHOICES
    }
    return render(request, 'phrases/about.html', context)

def get_phrase(request):
    """Gets a random motivational phrase from the selected category"""
    if request.method == 'POST':
        category = request.POST.get('category')
        
        # Get phrases from the selected category
        phrases = MotivationalPhrase.objects.filter(category=category)
        
        if phrases.exists():
            # Select a random phrase
            random_phrase = random.choice(phrases)
            return JsonResponse({
                'success': True,
                'phrase': random_phrase.text,
                'author': random_phrase.author if random_phrase.author else 'Anonymous'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'No phrases available for this category.'
            })
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'})
