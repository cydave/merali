FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONPATH "/app:${PYTHONPATH}"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--workers", "4", "--port", "8000"]
