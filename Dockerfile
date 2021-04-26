# образ на основе которого создаём контейнер
FROM python:3.9-alpine

# рабочая директория внутри проекта
WORKDIR /usr/src/app

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем зависимости
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# копируем содержимое текущей папки в контейнер
COPY . .