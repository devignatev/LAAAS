# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем содержимое текущей директории в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r src/requirements.txt

# Открываем порт (измените, если ваше приложение использует другой порт)
EXPOSE 8000

# Устанавливаем переменную окружения
ENV PYTHONPATH=/app

# Запускаем main.py при старте контейнера
CMD ["python", "src/main.py"]