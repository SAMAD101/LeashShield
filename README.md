# Get started .


## How to run this project locally:

- Install virtualenv python package to create a virtual environment.

```
pip install virtualenv
```

- Make and start a virtual environment.

For Linux/MacOS:
```
python -m venv .venv
source .venv/bin/activate
```

For Windows:
```
py -m venv .venv
source .venv/Scripts/activate

```

- Install the necessary libraries.

```
pip install -r requirements/development.txt
npm install bootstrap
```

- Migrate Django models.

```
python manage.py migrate users
python manage.py migrate
```

- Start the server.

```
python manage.py runserver
```
