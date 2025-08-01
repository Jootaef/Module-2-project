from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Contact, Project


def home(request):
    """Home page view with personal presentation"""
    context = {
        'title': 'Home - Portfolio',
        'name': 'Jaydan Smith',
        'title_profession': 'Full Stack Developer',
        'description': 'Passionate developer with expertise in web technologies and modern frameworks. I love creating innovative solutions and learning new technologies.',
        'skills': ['Python', 'Django', 'JavaScript', 'React', 'HTML/CSS', 'SQL', 'Git'],
        'experience_years': 3,
    }
    return render(request, 'main/home.html', context)


def projects(request):
    """Projects page view showing portfolio projects"""
    projects_list = Project.objects.all()
    context = {
        'title': 'Projects - Portfolio',
        'projects': projects_list,
    }
    return render(request, 'main/projects.html', context)


def contact(request):
    """Contact page view with form handling"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    context = {
        'title': 'Contact - Portfolio',
    }
    return render(request, 'main/contact.html', context)


def contact_ajax(request):
    """AJAX endpoint for contact form submission"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )
            return JsonResponse({
                'success': True,
                'message': 'Thank you! Your message has been sent successfully.'
            })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all fields.'
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}) 