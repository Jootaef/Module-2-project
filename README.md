# Overview

As a software engineer passionate about web development and modern technologies, I created this Portfolio Website to showcase my skills and projects while learning Django framework. This project represents my journey in mastering full-stack web development and creating professional, responsive web applications.

## Web Application Description

This Portfolio Website is a dynamic web application built with Django that serves as a professional portfolio for showcasing projects, skills, and providing a contact mechanism for potential clients or employers. The application features a modern, responsive design using Bootstrap 5 and includes three main pages: Home, Projects, and Contact.

### Starting the Test Server

To run the application locally:

1. Navigate to the project directory
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Populate database: `python populate_db.py`
5. Start the development server: `python manage.py runserver`
6. Open your browser and go to: **http://127.0.0.1:8000/**

The first page you'll see is the Home page with a professional presentation and navigation to other sections.

### Purpose

I developed this software to create a professional portfolio website that demonstrates my web development skills, showcases my projects, and provides an interactive way for potential clients or employers to contact me. This project helped me learn Django framework, database design, frontend development with Bootstrap, and implementing user interaction features like contact forms with AJAX functionality.

[Software Demo Video](http://youtube.link.goes.here)

# Web Pages

## Home Page

The home page serves as the main landing page with a hero section featuring my personal introduction, professional title, and description. It includes:

- **Dynamic content**: Personal information, skills list, and experience years are dynamically loaded from the Django view
- **Skills section**: Displays a list of technical skills as interactive badges
- **Services overview**: Three service cards showcasing web development, mobile development, and database design capabilities
- **Call-to-action**: Buttons linking to projects and contact pages

## Projects Page

The projects page displays a portfolio of my work with:

- **Dynamic project cards**: Projects are loaded from the database and displayed with images, descriptions, and technology tags
- **Interactive elements**: Each project card shows technologies used, GitHub links, and live demo links
- **Responsive grid**: Projects are displayed in a responsive grid that adapts to different screen sizes
- **Fallback content**: If no projects exist in the database, sample projects are displayed

## Contact Page

The contact page provides an interactive way for visitors to reach out:

- **Contact form**: Includes fields for name, email, and message with client-side validation
- **AJAX submission**: Form submissions are handled asynchronously without page reload
- **Database storage**: All contact messages are stored in the SQLite database
- **Success/error feedback**: Users receive immediate feedback on form submission
- **Contact information**: Displays additional contact details and social media links

### Page Transitions

Navigation between pages is handled through Django's URL routing system. The base template provides a consistent navigation bar that allows seamless movement between Home, Projects, and Contact pages. Each page extends the base template to maintain consistent styling and navigation.

# Development Environment

## Tools Used

- **Visual Studio Code**: Primary code editor with Python and Django extensions
- **Git**: Version control for tracking code changes
- **Windows PowerShell**: Command line interface for running Django commands
- **SQLite Browser**: Database management and inspection tool

## Programming Language and Libraries

### Backend

- **Python 3.12**: Primary programming language
- **Django 5.2.4**: Web framework for rapid development
- **SQLite3**: Lightweight database for development

### Frontend

- **HTML5**: Semantic markup structure
- **CSS3**: Custom styling with CSS variables and animations
- **JavaScript**: AJAX functionality for form submissions
- **Bootstrap 5.3.0**: Responsive CSS framework
- **Font Awesome 6.4.0**: Icon library for UI elements

### Key Libraries and Dependencies

- **asgiref 3.9.1**: ASGI utilities for Django
- **sqlparse 0.5.3**: SQL parsing library
- **tzdata 2025.2**: Timezone data

# Useful Websites

- [Django Documentation](https://docs.djangoproject.com/en/5.2/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/)
- [Font Awesome Icons](https://fontawesome.com/icons)
- [Django Tutorial](https://docs.djangoproject.com/en/5.2/intro/tutorial01/)
- [CSS Variables Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [JavaScript Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

# Future Work

- Implement user authentication system for admin access
- Add image upload functionality for project screenshots
- Integrate email notifications for contact form submissions
- Add blog section for technical articles and updates
- Implement dark/light theme toggle
- Add portfolio analytics and visitor tracking
- Create REST API for mobile app integration
- Add multi-language support (Spanish/English)
- Implement search functionality for projects
- Add project filtering by technology/category
- Integrate with external services (GitHub API, LinkedIn)
- Add portfolio download functionality (PDF generation)
- Implement caching for better performance
- Add unit tests and integration tests
