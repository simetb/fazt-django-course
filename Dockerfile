FROM python:3.8.19-slim
WORKDIR /app/
RUN pip install --upgrade pip
COPY django-project/requirements.txt .
RUN pip install -r requirements.txt
COPY django-project/ .
EXPOSE 8000
RUN chmod +x run.sh
