# Django Boilerplate

A modern Django project boilerplate using Poetry for dependency management.

## Requirements

- Python 3.8+
- Poetry
- PostgreSQL (recommended)

## Setup

1. Clone the repository:

```bash
git clone git@github.com:saadmakhdoom12/django-boilerplate.git
cd django-boilerplate
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Activate the virtual environment:

```bash
poetry shell
```

4. Set up environment variables:

```bash
cp .env.example .env
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start the development server:

```bash
python manage.py runserver
```

## Poetry Commands

- Install dependencies: `poetry install`
- Add a dependency: `poetry add package_name`
- Add a dev dependency: `poetry add --dev package_name`
- Update dependencies: `poetry update`
- Show dependency tree: `poetry show --tree`
- Export requirements: `poetry export -f requirements.txt --output requirements.txt`

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
```

### Code Formatting

```bash
black .
isort .
```

## Project Structure

```bash
django-boilerplate/
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .env.example
├── .gitignore
├── apps/
│   └── core/
├── config/
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
└── templates/
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
