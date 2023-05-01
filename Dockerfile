FROM python:latest
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY ./requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput --username administrator --email admin@admin.com
