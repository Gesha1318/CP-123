#!/bin/bash

# Django Intranet Management Script

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if we're in the right directory
check_directory() {
    if [ ! -f "intranet/manage.py" ]; then
        print_error "This script must be run from the project root directory (where docker-compose.yml is located)"
        exit 1
    fi
}

# Function to run Django management commands
run_django_command() {
    cd intranet
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    python manage.py "$@"
    cd ..
}

# Function to show help
show_help() {
    echo "Django Intranet Management Script"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  dev           Start development server"
    echo "  prod          Start production server"
    echo "  build         Build Docker image"
    echo "  up            Start services with docker-compose"
    echo "  down          Stop services"
    echo "  logs          Show service logs"
    echo "  shell         Open Django shell"
    echo "  migrate       Run database migrations"
    echo "  collectstatic Collect static files"
    echo "  createsuperuser Create superuser"
    echo "  test          Run tests"
    echo "  check         Check Django configuration"
    echo "  backup        Backup database"
    echo "  restore       Restore database from backup"
    echo "  help          Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 dev                    # Start development server"
    echo "  $0 prod                   # Start production server"
    echo "  $0 shell                  # Open Django shell"
    echo "  $0 migrate                # Run migrations"
}

# Function to start development server
start_dev() {
    print_status "Starting development server..."
    cd intranet
    if [ ! -d "venv" ]; then
        print_status "Creating virtual environment..."
        python3 -m venv venv
    fi
    
    if [ -d "venv" ]; then
        source venv/bin/activate
        print_status "Installing requirements..."
        pip install -r ../requirements.txt
    fi
    
    print_status "Running Django checks..."
    python manage.py check
    
    print_status "Running migrations..."
    python manage.py migrate
    
    print_status "Collecting static files..."
    python manage.py collectstatic --noinput
    
    print_status "Starting development server on http://localhost:8000"
    python manage.py runserver 0.0.0.0:8000
}

# Function to start production server
start_prod() {
    print_status "Starting production server with Docker..."
    docker-compose -f docker-compose.prod.yml up -d
    print_status "Production server started. Check logs with: $0 logs"
}

# Function to build Docker image
build_docker() {
    print_status "Building Docker image..."
    docker-compose build
    print_status "Docker image built successfully"
}

# Function to start services
start_services() {
    print_status "Starting services..."
    docker-compose up -d
    print_status "Services started. Check logs with: $0 logs"
}

# Function to stop services
stop_services() {
    print_status "Stopping services..."
    docker-compose down
    print_status "Services stopped"
}

# Function to show logs
show_logs() {
    print_status "Showing service logs..."
    docker-compose logs -f
}

# Function to backup database
backup_database() {
    print_status "Creating database backup..."
    if [ -f "intranet/db.sqlite3" ]; then
        cp intranet/db.sqlite3 "intranet/db_backup_$(date +%Y%m%d_%H%M%S).sqlite3"
        print_status "Database backed up successfully"
    else
        print_warning "No SQLite database found to backup"
    fi
}

# Function to restore database
restore_database() {
    if [ -z "$1" ]; then
        print_error "Please specify backup file to restore from"
        echo "Usage: $0 restore <backup_file>"
        exit 1
    fi
    
    if [ ! -f "intranet/$1" ]; then
        print_error "Backup file not found: $1"
        exit 1
    fi
    
    print_warning "This will overwrite your current database. Are you sure? (y/N)"
    read -r response
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        print_status "Restoring database from $1..."
        cp "intranet/$1" intranet/db.sqlite3
        print_status "Database restored successfully"
    else
        print_status "Database restore cancelled"
    fi
}

# Main script logic
check_directory

case "${1:-help}" in
    dev)
        start_dev
        ;;
    prod)
        start_prod
        ;;
    build)
        build_docker
        ;;
    up)
        start_services
        ;;
    down)
        stop_services
        ;;
    logs)
        show_logs
        ;;
    shell)
        run_django_command shell
        ;;
    migrate)
        run_django_command migrate
        ;;
    collectstatic)
        run_django_command collectstatic --noinput
        ;;
    createsuperuser)
        run_django_command createsuperuser
        ;;
    test)
        run_django_command test
        ;;
    check)
        run_django_command check
        ;;
    backup)
        backup_database
        ;;
    restore)
        restore_database "$2"
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac