#!/usr/bin/env python
"""
Script to populate the database with sample data for the Portfolio Website.
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from main.models import Project, Contact

def create_sample_projects():
    """Create sample projects for the portfolio"""
    projects_data = [
        {
            'title': 'E-Commerce Platform',
            'description': 'A full-featured e-commerce platform built with Django and React. Features include user authentication, product management, shopping cart, and payment integration with Stripe.',
            'technologies': 'Django, React, PostgreSQL, Stripe, Bootstrap',
            'github_url': 'https://github.com/jaydan/ecommerce-platform',
            'live_url': 'https://ecommerce-demo.com',
            'image': 'https://via.placeholder.com/400x200/3498db/ffffff?text=E-Commerce'
        },
        {
            'title': 'Task Management App',
            'description': 'A cross-platform mobile application for task management with real-time synchronization, team collaboration, and progress tracking features.',
            'technologies': 'React Native, Firebase, Redux, Node.js',
            'github_url': 'https://github.com/jaydan/task-manager',
            'live_url': 'https://task-manager-app.com',
            'image': 'https://via.placeholder.com/400x200/e74c3c/ffffff?text=Task+Manager'
        },
        {
            'title': 'Data Analytics Dashboard',
            'description': 'An interactive dashboard for data visualization and analytics. Features include real-time data processing, customizable charts, and export functionality.',
            'technologies': 'Python, D3.js, Flask, MongoDB',
            'github_url': 'https://github.com/jaydan/analytics-dashboard',
            'live_url': 'https://analytics-demo.com',
            'image': 'https://via.placeholder.com/400x200/2ecc71/ffffff?text=Analytics'
        },
        {
            'title': 'AI Chatbot',
            'description': 'An intelligent chatbot powered by machine learning for customer support. Features natural language processing and integration with multiple platforms.',
            'technologies': 'Python, TensorFlow, NLP, API',
            'github_url': 'https://github.com/jaydan/ai-chatbot',
            'live_url': 'https://chatbot-demo.com',
            'image': 'https://via.placeholder.com/400x200/9b59b6/ffffff?text=AI+Chatbot'
        },
        {
            'title': 'Portfolio Website',
            'description': 'A modern, responsive portfolio website built with Django and Bootstrap. Features dynamic content management and contact form functionality.',
            'technologies': 'Django, Bootstrap, SQLite, JavaScript',
            'github_url': 'https://github.com/jaydan/portfolio-website',
            'live_url': 'https://jaydan-portfolio.com',
            'image': 'https://via.placeholder.com/400x200/f39c12/ffffff?text=Portfolio'
        }
    ]
    
    for project_data in projects_data:
        project, created = Project.objects.get_or_create(
            title=project_data['title'],
            defaults=project_data
        )
        if created:
            print(f"✅ Created project: {project.title}")
        else:
            print(f"⏭️  Project already exists: {project.title}")

def create_sample_contacts():
    """Create sample contact messages"""
    contacts_data = [
        {
            'name': 'John Smith',
            'email': 'john.smith@company.com',
            'message': 'Hi Jaydan, I was impressed by your portfolio and would like to discuss a potential project. We need a web application for our startup and your skills seem perfect for the job.'
        },
        {
            'name': 'Sarah Johnson',
            'email': 'sarah.johnson@techcorp.com',
            'message': 'Hello! I saw your e-commerce project and it looks exactly like what we need. Can we schedule a call to discuss the requirements and timeline?'
        },
        {
            'name': 'Mike Davis',
            'email': 'mike.davis@startup.io',
            'message': 'Great work on the AI chatbot! We\'re looking for someone with ML experience for our customer service automation project. Are you available for freelance work?'
        }
    ]
    
    for contact_data in contacts_data:
        contact, created = Contact.objects.get_or_create(
            name=contact_data['name'],
            email=contact_data['email'],
            defaults=contact_data
        )
        if created:
            print(f"✅ Created contact: {contact.name}")
        else:
            print(f"⏭️  Contact already exists: {contact.name}")

def main():
    """Main function to populate the database"""
    print("🚀 Starting database population...")
    print("=" * 50)
    
    try:
        # Create sample projects
        print("\n📁 Creating sample projects...")
        create_sample_projects()
        
        # Create sample contacts
        print("\n📧 Creating sample contacts...")
        create_sample_contacts()
        
        print("\n" + "=" * 50)
        print("✅ Database population completed successfully!")
        print(f"📊 Created {Project.objects.count()} projects and {Contact.objects.count()} contacts")
        print("\n🎉 Your portfolio website is ready to use!")
        print("💡 Run 'python manage.py runserver' to start the development server")
        
    except Exception as e:
        print(f"❌ Error populating database: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main() 