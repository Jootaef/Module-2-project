#!/usr/bin/env python
import os
import django

# Configure Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'motivational_phrases.settings')
django.setup()

from phrases.models import MotivationalPhrase

def populate_database():
    """Populate the database with sample motivational phrases"""
    
    phrases_data = [
        # Work
        {
            'category': 'work',
            'text': 'Success is not final, failure is not fatal: it is the courage to continue that counts.',
            'author': 'Winston Churchill'
        },
        {
            'category': 'work',
            'text': 'Quality remains long after the price is forgotten.',
            'author': 'Aldo Gucci'
        },
        {
            'category': 'work',
            'text': 'Hard work beats talent when talent doesn\'t work hard.',
            'author': 'Tim Notke'
        },
        {
            'category': 'work',
            'text': 'Innovation distinguishes between a leader and a follower.',
            'author': 'Steve Jobs'
        },
        
        # Study
        {
            'category': 'study',
            'text': 'Education is the most powerful weapon which you can use to change the world.',
            'author': 'Nelson Mandela'
        },
        {
            'category': 'study',
            'text': 'Knowledge is power. Information is liberating.',
            'author': 'Kofi Annan'
        },
        {
            'category': 'study',
            'text': 'Learning never exhausts the mind.',
            'author': 'Leonardo da Vinci'
        },
        {
            'category': 'study',
            'text': 'The mind is not a vessel to be filled, but a fire to be kindled.',
            'author': 'Plutarch'
        },
        
        # Love
        {
            'category': 'love',
            'text': 'Love is not something you look at, it is something you feel. And even more, it is something you demonstrate.',
            'author': 'Paulo Coelho'
        },
        {
            'category': 'love',
            'text': 'Love is patient, love is kind.',
            'author': 'Bible'
        },
        {
            'category': 'love',
            'text': 'Love does not consist in gazing at each other, but in looking outward together in the same direction.',
            'author': 'Antoine de Saint-Exupéry'
        },
        {
            'category': 'love',
            'text': 'Love is the poetry of the senses.',
            'author': 'Honoré de Balzac'
        },
        
        # Sports
        {
            'category': 'sports',
            'text': 'Sports do not build character. They reveal it.',
            'author': 'Heywood Broun'
        },
        {
            'category': 'sports',
            'text': 'Champions aren\'t made in gyms. Champions are made from something they have deep inside them.',
            'author': 'Muhammad Ali'
        },
        {
            'category': 'sports',
            'text': 'Pain is temporary. It may last a minute, or an hour, or a day, or a year, but eventually it will subside.',
            'author': 'Lance Armstrong'
        },
        {
            'category': 'sports',
            'text': 'The difference between the impossible and the possible lies in determination.',
            'author': 'Tommy Lasorda'
        },
        
        # Life
        {
            'category': 'life',
            'text': 'Life is what happens while you\'re busy making other plans.',
            'author': 'John Lennon'
        },
        {
            'category': 'life',
            'text': 'Don\'t count the days, make the days count.',
            'author': 'Muhammad Ali'
        },
        {
            'category': 'life',
            'text': 'Life is either a daring adventure or nothing at all.',
            'author': 'Helen Keller'
        },
        {
            'category': 'life',
            'text': 'The purpose of life is to live it, to taste experience to the utmost.',
            'author': 'Eleanor Roosevelt'
        },
        {
            'category': 'life',
            'text': 'Happiness is not something you postpone for the future; it is something you design for the present.',
            'author': 'Jim Rohn'
        }
    ]
    
    # Create phrases in the database
    for phrase_data in phrases_data:
        MotivationalPhrase.objects.get_or_create(
            text=phrase_data['text'],
            category=phrase_data['category'],
            defaults={
                'author': phrase_data['author']
            }
        )
    
    print(f"✅ Database populated with {len(phrases_data)} motivational phrases")
    print("📊 Phrases by category:")
    
    for category_code, category_name in MotivationalPhrase.CATEGORY_CHOICES:
        count = MotivationalPhrase.objects.filter(category=category_code).count()
        print(f"   - {category_name}: {count} phrases")

if __name__ == '__main__':
    populate_database() 