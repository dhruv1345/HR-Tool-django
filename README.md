
# HR Tool - Django Based File Tracker

A simple Django-based file tracking system with user authentication, version history, and enhanced UI features.

## Features

- User registration and login system.
- Upload and edit text files.
- Maintain file version history.
- Beautiful UI using Bootstrap 5 and Django Crispy Forms.
- Rich Text Editing using CKEditor.
- Syntax Highlighting for code using CodeMirror.

## Installation

1. Clone the repository:

```bash
git clone git@github.com:dhruv1345/HR-Tool-django.git
cd HR-Tool-django
```

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

## Usage

- Register or login as a user.
- Upload files and view/edit them.
- See file version history.

## Media and Static Files

Ensure you configure media handling in `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

And in `urls.py` (for development):

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## Tech Stack

- Django
- Bootstrap 5 (via CDN)
- Django Crispy Forms
- CKEditor (for rich text)
- CodeMirror (for syntax highlighting)

## License

MIT License.
