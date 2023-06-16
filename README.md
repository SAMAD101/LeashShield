# Get started

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



# Process to Setup Frontend
## :information_source: Requirements

- [Node.js](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/)
  
**Fork/Clone the repository then**
**move to reactapp**

```
cd reactapp
```

**To install this project**

```
npm install
```

**To run the server**

```
npm start
```

**To build the app**

```
npm run build
```

---
