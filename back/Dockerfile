FROM python:3.6-alpine

WORKDIR /app

COPY ./requirements.txt .

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "api.py"]
