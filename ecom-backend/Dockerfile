FROM python:3.12.12-slim

WORKDIR /ecom-backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /ecom-backend/logs \
    && touch /ecom-backend/logs/app_errors.log

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "3050"]
