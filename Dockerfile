# Use official Python runtime as a parent image
FROM python:3.11-slim
ARG WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONPATH="${WORKDIR}"

EXPOSE ${PORT}
COPY requirements.txt /temp/requirements.txt
RUN pip install --no-cache-dir -r /temp/requirements.txt && rm -rf /temp/requirements.txt
COPY app/ ./app/
CMD ["python", "app/main.py"]
