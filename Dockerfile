FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD ./ /code/
RUN python djangoProject/manage.py makemigrations

RUN python djangoProject/manage.py migrate
EXPOSE 80
#CMD ["python", "djangoProject/manage.py", "runserver", "0.0.0.0:80"]
CMD exec gunicorn djangoProject.wsgi:application --bind 0.0.0.0:80 --workers 3
