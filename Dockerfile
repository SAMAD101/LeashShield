FROM python:3.8

WORKDIR /app

COPY . . 

RUN pip install -r requirements/development.txt 

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

CMD ["python", "manage.py", "runserver"]