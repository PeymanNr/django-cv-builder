FROM python:3.10-slim

LABEL maintainer="Peyman Naseri ipeymman@gmail.com"

WORKDIR /src

COPY requirements.txt /src
RUN pip install -r requirements.txt

COPY . /src

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

