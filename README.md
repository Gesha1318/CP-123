# Django Intranet System

A modern, secure intranet system built with Django, featuring document management, section-based organization, and role-based access control.

## Features

- **Section Management**: Hierarchical organization of content with public/private access control
- **Document Management**: Articles and file uploads with version control
- **User Management**: Role-based permissions and section memberships
- **Modern Admin Interface**: Beautiful admin interface powered by Django Jazzmin
- **REST API**: Full REST API support for integration
- **Security**: Production-ready security configurations
- **Docker Support**: Containerized deployment with Docker and Docker Compose
- **Multi-language**: Russian and English language support

## Technology Stack

- **Backend**: Django 5.2+
- **Database**: SQLite (development) / PostgreSQL (production)
- **Admin Interface**: Django Jazzmin
- **Authentication**: Django Allauth
- **API**: Django REST Framework
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Deployment**: Docker, Nginx, Gunicorn

## Quick Start

### Prerequisites

- Python 3.11+
- Docker and Docker Compose (for production)
- Git

### Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Gesha1318/CP-123.git
   cd CP-123
   ```

2. **Use the management script (recommended)**
   ```bash
   ./manage.sh dev
   ```

3. **Manual setup (alternative)**
   ```bash
   cd intranet
   python3 -m venv venv
   source venv/bin/activate
   pip install -r ../requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   python manage.py runserver
   ```

4. **Create a superuser**
   ```bash
   ./manage.sh createsuperuser
   ```

5. **Access the application**
   - Main site: http://localhost:8000
   - Admin interface: http://localhost:8000/admin

### Production Deployment

1. **Set up environment variables**
   ```bash
   cp .env.production.example .env.production
   # Edit .env.production with your production values
   ```

2. **Deploy with Docker**
   ```bash
   ./manage.sh prod
   ```

3. **Or use the management script**
   ```bash
   ./manage.sh build
   ./manage.sh up
   ```

## Project Structure

```
CP-123/
├── intranet/                 # Django project root
│   ├── intranet/            # Project settings
│   ├── core/                # Core app with common functionality
│   ├── accounts/            # User management and permissions
│   ├── sections/            # Section management
│   ├── documents/           # Document and file management
│   ├── templates/           # HTML templates
│   ├── static/              # Static files (CSS, JS)
│   └── manage.py            # Django management script
├── docker-compose.yml       # Development Docker configuration
├── docker-compose.prod.yml  # Production Docker configuration
├── Dockerfile               # Docker image definition
├── nginx.conf               # Nginx configuration
├── manage.sh                # Management script
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## Apps Overview

### Core App
- Common functionality and utilities
- Custom template tags
- Admin customizations

### Accounts App
- User role management
- Section membership and permissions
- Custom user admin interface

### Sections App
- Hierarchical section organization
- Public/private access control
- Section member management

### Documents App
- Article creation and management
- File uploads and storage
- Content versioning

## Management Commands

The project includes a comprehensive management script (`manage.sh`) for common operations:

```bash
# Development
./manage.sh dev              # Start development server
./manage.sh shell            # Open Django shell
./manage.sh migrate          # Run migrations
./manage.sh test             # Run tests

# Production
./manage.sh prod             # Start production server
./manage.sh build            # Build Docker image
./manage.sh up               # Start services
./manage.sh down             # Stop services
./manage.sh logs             # View logs

# Database
./manage.sh backup           # Backup database
./manage.sh restore <file>   # Restore from backup
```

## Configuration

### Environment Variables

Key environment variables for configuration:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Enable/disable debug mode
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_*`: Database connection settings
- `CORS_*`: CORS configuration
- `EMAIL_*`: Email server configuration

### Security Settings

The project includes comprehensive security configurations:

- HTTPS enforcement (production)
- HSTS headers
- XSS protection
- CSRF protection
- Secure cookies
- Rate limiting (via Nginx)

## API Endpoints

The system provides a REST API for integration:

- **Authentication**: Session-based authentication
- **Sections**: CRUD operations for sections
- **Documents**: Article and file management
- **Users**: User and permission management

## Customization

### Adding New Apps

1. Create the app: `python manage.py startapp myapp`
2. Add to `INSTALLED_APPS` in settings
3. Include URLs in main `urls.py`
4. Create models, views, and templates

### Customizing Admin Interface

The admin interface is powered by Django Jazzmin. Customize by modifying:

- `JAZZMIN_SETTINGS` in settings.py
- `JAZZMIN_UI_TWEAKS` for UI customization
- Custom admin classes in each app's `admin.py`

### Styling

- Main styles: `intranet/static/css/app.css`
- Bootstrap 5 is included via CDN
- Customize templates in `templates/` directory

## Deployment

### Development

- SQLite database
- Django development server
- Debug mode enabled
- Local static file serving

### Production

- PostgreSQL database
- Gunicorn application server
- Nginx reverse proxy
- Static file optimization
- Security headers enabled
- SSL/TLS encryption

## Troubleshooting

### Common Issues

1. **Database errors**: Run `./manage.sh migrate`
2. **Static files not loading**: Run `./manage.sh collectstatic`
3. **Permission errors**: Check file ownership in Docker
4. **Port conflicts**: Change ports in docker-compose.yml

### Logs

- Django logs: `intranet/django.log`
- Docker logs: `./manage.sh logs`
- Nginx logs: Available in Docker container

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:

- Create an issue on GitHub
- Check the documentation
- Review the code examples

## Changelog

### Version 1.0.0
- Initial release
- Basic intranet functionality
- User management and permissions
- Document management
- Section organization
- Docker deployment support
- Production security configurations