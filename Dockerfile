FROM python:3.10-slim

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY todolist/ .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]