FROM python:3.6

WORKDIR /opt/app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install  /opt/app/.


ENV FLASK_APP app.py

EXPOSE 8000
