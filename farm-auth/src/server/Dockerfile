FROM python:3.9-alpine

WORKDIR /code
COPY ./app /code/app
COPY ./main.py /code
COPY ./requirements.txt /code
COPY .env /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]