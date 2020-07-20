FROM python:3.8-slim

WORKDIR /src

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./client.py" ]
