# За базу используем официальный image питона
FROM python:3.10.6

# Отключаем буферизацию логов
ENV PYTHONUNBUFFERED 1

# Обновляем пакетный менеджер
RUN pip install --upgrade pip

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
