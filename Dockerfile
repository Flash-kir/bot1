# syntax=docker/dockerfile:1

FROM python:3.6-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY devman_bot.py .
CMD ["python", "devman_bot.py"]