# Используем официальный образ Python
FROM python:3.9-slim

# Установка зависимостей
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY app/ app/

# Устанавливаем переменную окружения для FastAPI
ENV PYTHONPATH=/app

# Запускаем приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
