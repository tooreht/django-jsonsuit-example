# django-jsonsuit-example

This is a demo project on how to use [django-jsonsuit](https://github.com/tooreht/django-jsonsuit) in a [Django](https://docs.djangoproject.com/) project.

Have a look at the source code to see some example usages of django-jsonsuit.

Also have a look at the [offical documentation](https://tooreht.github.io/django-jsonsuit/).

## Quickstart

1. Clone this project:

        git clone https://tooreht.github.io/django-jsonsuit-example

1. Navigate into the cloned project:

        cd django-jsonsuit-example

1. Create a virtualenv:

        python -m venv venv

1. Activate the virtualenv:

    On Unix

        ./venv/bin/activate

   On Windows (PowerShell)

        ./venv/Scripts/activate

1. Install requirements:

        pip install -r requirements.txt

1. Navigate to the example_project:

        cd example_project

1. Apply migrations

        python manage.py migrate

1. Create superuser for Django Admin

        python manage.py createsuperuser

1. Start the Django dev server:

        python .\manage.py runserver

1. Open the [demo page](http://localhost:8000/) in your browser
