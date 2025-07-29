# 🎯 Motivational Phrase Generator

## 📋 Project Description

This is a **Motivational Phrase Generator** developed with Django that allows users to select a specific category and get a random motivational phrase corresponding to that category.

## ✨ Features

- **Modern and attractive interface** with responsive design
- **5 phrase categories**: Work, Study, Love, Sports, and Life
- **Random generation** of phrases by category
- **SQLite database** with 21 predefined motivational phrases
- **2 dynamic HTML pages**: Main page and information page
- **Complete interactivity** with JavaScript and AJAX

## 🚀 Requirements Met

| Requirement                 | Status | Description                              |
| --------------------------- | ------ | ---------------------------------------- |
| ✅ Web framework (Django)   | Met    | Complete web application with Django     |
| ✅ 2 dynamic HTML pages     | Met    | Main page and "About" page               |
| ✅ User input interactivity | Met    | Category selection and phrase generation |
| ✅ Local execution          | Met    | Django development server                |
| ✅ Database (SQLite)        | Met    | Django model with SQLite                 |

## 🛠️ Technologies Used

- **Backend**: Django 5.2.4
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Language**: Python 3.12

## 📦 Installation and Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone or download the project**

   ```bash
   # Navigate to the project directory
   cd "path/to/project"
   ```

2. **Install dependencies**

   ```bash
   pip install django
   ```

3. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Populate database with sample phrases**

   ```bash
   python populate_db.py
   ```

5. **Start development server**

   ```bash
   python manage.py runserver
   ```

6. **Open in browser**
   ```
   http://127.0.0.1:8000/
   ```

## 🎮 How to Use the Application

1. **Access the application**: Open your browser and go to `http://127.0.0.1:8000/`

2. **Select category**: Choose one of the 5 available categories:

   - 🏢 **Work**: Motivational phrases for the workplace
   - 📚 **Study**: Phrases for students and learning
   - ❤️ **Love**: Phrases about relationships and love
   - 🏃 **Sports**: Phrases for sports motivation
   - 🌟 **Life**: General life phrases

3. **Generate phrase**: Click "🎯 Get Phrase" to receive a random phrase

4. **View information**: Click "📚 About the Project" to see statistics and details

## 📊 Project Structure

```
motivational_phrases/
├── manage.py                 # Django management script
├── motivational_phrases/     # Main project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URLs
│   ├── wsgi.py
│   └── asgi.py
├── phrases/                  # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # MotivationalPhrase model
│   ├── views.py             # Application views
│   ├── urls.py              # Application URLs
│   └── templates/           # HTML templates
│       └── phrases/
│           ├── base.html    # Base template
│           ├── home.html    # Main page
│           └── about.html   # Information page
├── db.sqlite3               # SQLite database
├── populate_db.py           # Database population script
└── README.md               # This file
```

## 🗄️ Data Model

### MotivationalPhrase

- **category**: Phrase category (work, study, love, sports, life)
- **text**: Motivational phrase text
- **author**: Phrase author (optional)
- **created_at**: Creation date (automatic)

## 🎨 Interface Features

- **Modern design** with gradients and shadows
- **Responsive design** that adapts to different devices
- **Smooth animations** on buttons and interactive elements
- **Intuitive interface** with attractive icons and colors
- **Visual feedback** during phrase loading

## 🔧 Technical Features

- **AJAX**: Asynchronous communication to get phrases without page reload
- **CSRF Protection**: Protection against CSRF attacks
- **JSON Responses**: JSON format responses for the API
- **Template Inheritance**: HTML code reuse with base templates
- **Database Queries**: Optimized database queries

## 📈 Project Statistics

- **Total phrases**: 21 motivational phrases
- **Categories**: 5 different categories
- **Authors**: 15+ recognized authors
- **HTML pages**: 2 dynamic pages
- **Code lines**: ~500 lines of Python/HTML/CSS/JS code

## 🚀 Useful Commands

```bash
# Create superuser (optional)
python manage.py createsuperuser

# Access Django shell
python manage.py shell

# Run tests (if implemented)
python manage.py test

# Collect static files (for production)
python manage.py collectstatic
```

## 🤝 Contributions

This project was developed as part of an academic course. Contributions are welcome to improve functionality and design.

## 📝 License

This project is for educational use and is available under MIT license.

---

**Developed with ❤️ using Django**
